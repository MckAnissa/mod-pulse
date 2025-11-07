from __future__ import annotations
import argparse
from .ui import list_cmd, watch_cmd

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mod-pulse", description="Simple mod watcher")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("list", help="List detected mods")
    sp.add_argument("--root", default=None)
    sp.set_defaults(func=lambda a: list_cmd(a.root))

    sp = sub.add_parser("watch", help="Live-refresh when mods change")
    sp.add_argument("--root", default=None)
    sp.add_argument("--interval", type=float, default=2.0)
    sp.set_defaults(func=lambda a: watch_cmd(a.root, a.interval))
    return p

def main() -> None:
    args = _build_parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
