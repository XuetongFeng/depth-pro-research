#!/usr/bin/env python3
"""Validate a Depth Pro evaluation manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_IMAGE_KEYS = {
    "id",
    "path",
    "source",
    "license",
    "bucket",
    "has_exif_focal_length",
    "notes",
}


def validate_manifest(path: Path) -> None:
    manifest = json.loads(path.read_text(encoding="utf-8"))

    for key in ("project", "version", "model", "images", "outputs"):
        if key not in manifest:
            raise SystemExit(f"manifest missing key: {key}")

    if manifest["project"] != "depth-pro-research":
        raise SystemExit("project must be depth-pro-research")

    images = manifest["images"]
    if not isinstance(images, list) or not images:
        raise SystemExit("images must be a non-empty list")

    seen_ids: set[str] = set()
    for index, image in enumerate(images, start=1):
        missing = REQUIRED_IMAGE_KEYS - image.keys()
        if missing:
            raise SystemExit(f"image #{index} missing keys: {sorted(missing)}")
        if image["id"] in seen_ids:
            raise SystemExit(f"duplicate image id: {image['id']}")
        seen_ids.add(image["id"])
        if not isinstance(image["has_exif_focal_length"], bool):
            raise SystemExit(f"{image['id']}: has_exif_focal_length must be boolean")

    print(f"Validated {len(images)} image entries.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "manifest",
        nargs="?",
        default="configs/eval_manifest.example.json",
        help="Path to evaluation manifest JSON.",
    )
    args = parser.parse_args()
    validate_manifest(Path(args.manifest))


if __name__ == "__main__":
    main()

