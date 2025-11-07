# src/scanner.py
from __future__ import annotations
from pathlib import Path
from typing import Iterable

def scan(root: str | Path) -> list[dict]:
    """Return a list of mods under root with a simple manifest check."""
    p = Path(root)
    mods: list[dict] = []
    if not p.exists():
        return mods

    for d in p.iterdir():
        if not d.is_dir():
            continue
        manifest = d / "manifest.toml"
        mods.append({
            "name": d.name,
            "path": str(d),
            "has_manifest": manifest.exists(),
        })
    return mods
