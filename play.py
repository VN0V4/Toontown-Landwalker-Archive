"""Run an old (2017-2018, Windows + Python 2) Toontown script on modern Panda3D.

The script files themselves are never modified. Two fixes are applied in memory:
  - Windows-style asset paths ('phase_4\\models/foo.bam') get forward slashes.
  - Python 2 print statements ('print "hi"') become print() calls.

Usage: ./play.sh Estate.py   (run from anywhere; paths are relative to Toontown/Toontown)
"""
import os
import re
import sys

GAME_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Toontown", "Toontown")

ASSET_STRING = re.compile(r"""(['"])([^'"\n]*\\[^'"\n]*)\1""")
ASSET_HINT = re.compile(r"phase_|\.(bam|egg|jpg|png|rgb|mp3|ogg|wav|ttf|cur|ico)\b", re.I)
PRINT_STMT = re.compile(r"^(\s*)print(?!\s*\()\s+(.+?)\s*$", re.M)


def fix_path(match):
    quote, body = match.groups()
    if not ASSET_HINT.search(body):
        return match.group(0)  # a real escape like '\n', leave it alone
    return quote + body.replace("\\", "/") + quote


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    script = sys.argv[1]
    if not os.path.isabs(script) and not os.path.exists(script):
        script = os.path.join(GAME_DIR, script)
    script = os.path.abspath(script)

    with open(script, encoding="utf-8", errors="replace") as f:
        source = f.read()
    source = ASSET_STRING.sub(fix_path, source)
    source = PRINT_STMT.sub(r"\1print(\2)", source)

    # Behave like `python Script.py` run from the script's own folder (what the .bat files did).
    os.chdir(os.path.dirname(script))
    sys.path.insert(0, os.path.dirname(script))
    # Panda looks up models on its model path (which starts at $MAIN_DIR, i.e. this launcher's folder),
    # not the working directory, so put the script's folder first.
    from panda3d.core import Filename, getModelPath
    getModelPath().prependDirectory(Filename.fromOsSpecific(os.path.dirname(script)))
    sys.argv = [script] + sys.argv[2:]
    code = compile(source, script, "exec")
    exec(code, {"__name__": "__main__", "__file__": script})


if __name__ == "__main__":
    main()
