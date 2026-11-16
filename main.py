"""Bow to the Stars -- make.fun ai-excited-01 entry.

This program copies the bundled picture to the grader's output
directory. The picture lives next to this file as entry.png. The grader
runs the program twice and both runs must write identical bytes, so the
program only copies bytes and never re-encodes anything.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    """Return the hex sha256 digest of the file at path."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    if not os.path.isfile(source):
        print("error: bundled entry.png not found next to main.py",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")

    shutil.copyfile(source, target)

    # Read-back check: the written file must be byte-identical to the
    # bundled picture, otherwise this run is not deterministic.
    if sha256_of(source) != sha256_of(target):
        print("error: output does not match bundled entry.png",
              file=sys.stderr)
        return 1

    print("wrote %s (%s)" % (target, sha256_of(target)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
