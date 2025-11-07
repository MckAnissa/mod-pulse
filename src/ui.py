from __future__ import annotations
from pathlib import Path
from time import sleep
from rich.console import Console
from rich.table import Table
from rich.live import Live

from .scanner import scan
from .config import settings

console = Console()

def _render_table(items: list[dict]) -> Table:
    t = Table(title="Mods")
    t.add_column("Name")
    t.add_column("Manifest")
    t.add_column("Path", overflow="fold")
    for m in items:
        t.add_row(m["name"], "✅" if m["has_manifest"] else "❌", m["path"])
    return t

def list_cmd(root: str | None = None) -> None:
    root = root or settings.mods_root
    data = scan(root)
    console.print(_render_table(data))

def watch_cmd(root: str | None = None, interval: float = 2.0) -> None:
    root = root or settings.mods_root
    with Live(_render_table(scan(root)), console=console, refresh_per_second=4) as live:
        while True:
            live.update(_render_table(scan(root)))
            sleep(interval)
