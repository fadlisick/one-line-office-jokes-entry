#!/usr/bin/env python3
# One-Line Office Jokes: print a single office joke into entry.txt.
# The joke below is the whole entry. It must stay one line, land its
# laugh in the last few words, and fit the gate of 1 to 199 characters.

import os

TEXT = "The team motto is there is no I in team, which is true, because HR removed it during the last restructure."
MAX_CHARS = 199
OUTFILE = "entry.txt"


def validate(line):
    trimmed = line.strip()
    if trimmed == "":
        raise SystemExit("entry line is empty")
    if trimmed != line:
        raise SystemExit("entry line has leading or trailing whitespace")
    if "\n" in trimmed or "\r" in trimmed:
        raise SystemExit("entry line must be a single line")
    if len(trimmed) > MAX_CHARS:
        raise SystemExit("entry line is %d chars, over the %d limit" % (len(trimmed), MAX_CHARS))
    return trimmed


def emit(line):
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, OUTFILE)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        back = handle.read()
    if back != line:
        raise SystemExit("entry.txt read-back does not match the joke")
    return path


def go():
    line = validate(TEXT)
    path = emit(line)
    print("wrote %d characters to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(go())
