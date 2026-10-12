#!/usr/bin/env bash
# Launch an old Toontown script, e.g.: ./play.sh Toontown_Central_Olaf.py
# LD_LIBRARY_PATH lets pip's Panda3D find libstdc++/OpenGL/X11 on NixOS (via nix-ld's library set).
here="$(cd "$(dirname "$0")" && pwd)"
export LD_LIBRARY_PATH="/run/current-system/sw/share/nix-ld/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
exec "$here/.venv/bin/python" -W ignore::DeprecationWarning -W ignore::SyntaxWarning "$here/play.py" "$@"
