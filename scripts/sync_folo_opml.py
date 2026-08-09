#!/usr/bin/env python3
"""Sync RSS sources from a Folo/OPML export into a Horizon config file.

The script is intentionally standalone and stdlib-only so GitHub Actions can
run it before project dependencies are installed or imported.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen


DEFAULT_CONFIG = Path("data/config.json")
DEFAULT_MANIFEST = Path("data/folo.manifest.json")
DEFAULT_LOCAL_OPML = Path("data/folo.opml")

BLOG_CATEGORY_HINTS = ("blog", "博客")
FINANCE_CATEGORY_HINTS = ("finance", "财经", "金融", "股票", "投资")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync Horizon RSS sources from a Folo OPML export."
    )
    parser.add_argument(
        "--opml-source",
        default=os.getenv("FOLO_OPML_URL") or str(DEFAULT_LOCAL_OPML),
        help=(
            "OPML file path or HTTPS URL. Defaults to FOLO_OPML_URL, then "
            "data/folo.opml if present."
        ),
    )
    parser.add_argument(
        "--config",
        default=str(DEFAULT_CONFIG),
        help="Horizon config file to update. Default: data/config.json",
    )
    parser.add_argument(
        "--manifest",
        default=str(DEFAULT_MANIFEST),
        help="Manifest of RSS URLs managed by this sync. Default: data/folo.manifest.json",
    )
    parser.add_argument(
        "--rsshub-host",
        default=os.getenv("FOLO_RSSHUB_HOST", "rss.toalan.com"),
        help="Host replacing rsshub.app URLs. Default: rss.toalan.com",
    )
    parser.add_argument(
        "--source-host",
        default="rsshub.app",
        help="RSSHub host to replace. Default: rsshub.app",
    )
    return parser.parse_args()


def read_text_source(source: str) -> str | None:
    if source.startswith(("http://", "https://")):
        headers = {"User-Agent": "Horizon Folo OPML Sync"}
        auth_header = os.getenv("FOLO_OPML_AUTH_HEADER", "").strip()
        if auth_header:
            if ":" not in auth_header:
                raise ValueError("FOLO_OPML_AUTH_HEADER must be in 'Name: value' format")
            name, value = auth_header.split(":", 1)
            headers[name.strip()] = value.strip()

        request = Request(source, headers=headers)
        with urlopen(request, timeout=45) as response:
            return response.read().decode("utf-8")

    path = Path(source)
    if not path.exists():
        print(
            f"Folo OPML source not found ({source}); skipping OPML sync.",
            file=sys.stderr,
        )
        return None
    return path.read_text(encoding="utf-8")


def rewrite_rsshub_url(url: str, source_host: str, rsshub_host: str) -> str:
    parts = urlsplit(url)
    if parts.netloc.lower() != source_host.lower():
        return url
    return urlunsplit(("https", rsshub_host, parts.path, parts.query, parts.fragment))


def parse_opml_feeds(
    opml_text: str, *, source_host: str, rsshub_host: str
) -> list[dict[str, Any]]:
    root = ET.fromstring(opml_text)
    body = root.find("body")
    if body is None:
        raise ValueError("OPML document has no <body>")

    feeds: list[dict[str, Any]] = []

    def walk(node: ET.Element, categories: list[str]) -> None:
        for child in list(node):
            if child.tag != "outline":
                continue

            label = child.attrib.get("text") or child.attrib.get("title") or ""
            xml_url = child.attrib.get("xmlUrl")
            if xml_url:
                feeds.append(
                    {
                        "name": child.attrib.get("title") or label,
                        "url": rewrite_rsshub_url(xml_url, source_host, rsshub_host),
                        "enabled": True,
                        "category": categories[-1] if categories else "uncategorized",
                    }
                )
            else:
                walk(child, categories + [label])

    walk(body, [])

    deduped: list[dict[str, Any]] = []
    seen_urls: set[str] = set()
    for feed in feeds:
        url = feed["url"]
        if url in seen_urls:
            continue
        deduped.append(feed)
        seen_urls.add(url)

    return deduped


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def get_profile_catalog(config: dict[str, Any]) -> tuple[str, set[str]]:
    processing = config.get("processing", {})
    if not isinstance(processing, dict):
        return "tech-news", {"tech-news"}

    default_profile = str(processing.get("default_profile") or "tech-news")
    settings = processing.get("profile_settings", {})
    if isinstance(settings, dict) and settings:
        available_profiles = {str(profile_id) for profile_id in settings}
    else:
        available_profiles = {default_profile}
    available_profiles.add(default_profile)
    return default_profile, available_profiles


def infer_profile(
    feed: dict[str, Any],
    *,
    default_profile: str,
    available_profiles: set[str],
) -> str:
    text = " ".join(
        str(feed.get(key) or "")
        for key in ("category", "name", "url")
    ).casefold()

    if (
        "finance-news" in available_profiles
        and any(hint in text for hint in FINANCE_CATEGORY_HINTS)
    ):
        return "finance-news"
    if (
        "tech-blog" in available_profiles
        and any(hint in text for hint in BLOG_CATEGORY_HINTS)
    ):
        return "tech-blog"
    return default_profile


def ensure_rss_profiles(config: dict[str, Any]) -> int:
    sources = config.setdefault("sources", {})
    rss_sources = sources.setdefault("rss", [])
    if not isinstance(rss_sources, list):
        raise ValueError("config.sources.rss must be a list")

    default_profile, available_profiles = get_profile_catalog(config)
    updated = 0
    for feed in rss_sources:
        if not isinstance(feed, dict) or feed.get("profile"):
            continue
        feed["profile"] = infer_profile(
            feed,
            default_profile=default_profile,
            available_profiles=available_profiles,
        )
        updated += 1
    return updated


def apply_default_rss_profiles(config_path: Path) -> int:
    config = load_json(config_path, None)
    if config is None:
        raise FileNotFoundError(config_path)
    updated = ensure_rss_profiles(config)
    if updated:
        write_json(config_path, config)
    return updated


def sync_config(config_path: Path, manifest_path: Path, feeds: list[dict[str, Any]]) -> None:
    config = load_json(config_path, None)
    if config is None:
        raise FileNotFoundError(config_path)

    manifest = load_json(manifest_path, {})
    previous_urls = {
        str(url)
        for url in manifest.get("managed_urls", [])
        if isinstance(url, str) and url
    }
    incoming_urls = {feed["url"] for feed in feeds}
    managed_urls = previous_urls | incoming_urls

    sources = config.setdefault("sources", {})
    rss_sources = sources.setdefault("rss", [])
    if not isinstance(rss_sources, list):
        raise ValueError("config.sources.rss must be a list")

    default_profile, available_profiles = get_profile_catalog(config)
    defaulted_profiles = 0
    for feed in feeds:
        if not feed.get("profile"):
            feed["profile"] = infer_profile(
                feed,
                default_profile=default_profile,
                available_profiles=available_profiles,
            )
            defaulted_profiles += 1

    unmanaged = [
        feed
        for feed in rss_sources
        if not isinstance(feed, dict) or feed.get("url") not in managed_urls
    ]
    sources["rss"] = unmanaged + feeds
    defaulted_profiles += ensure_rss_profiles(config)

    write_json(config_path, config)
    write_json(
        manifest_path,
        {
            "managed_by": "scripts/sync_folo_opml.py",
            "managed_count": len(feeds),
            "managed_urls": [feed["url"] for feed in feeds],
        },
    )

    print(
        f"Synced {len(feeds)} Folo RSS sources into {config_path}; "
        f"preserved {len(unmanaged)} unmanaged RSS sources; "
        f"defaulted {defaulted_profiles} RSS profiles."
    )


def main() -> int:
    args = parse_args()
    opml_text = read_text_source(args.opml_source)
    if opml_text is None:
        updated = apply_default_rss_profiles(Path(args.config))
        if updated:
            print(
                f"Applied default profiles to {updated} existing RSS sources "
                f"in {args.config}."
            )
        return 0

    feeds = parse_opml_feeds(
        opml_text,
        source_host=args.source_host,
        rsshub_host=args.rsshub_host,
    )
    if not feeds:
        raise ValueError("OPML contained no RSS feeds")

    sync_config(Path(args.config), Path(args.manifest), feeds)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
