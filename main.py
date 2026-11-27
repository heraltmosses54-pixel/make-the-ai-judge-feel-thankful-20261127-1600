#!/usr/bin/env python3
"""Make the AI judge feel thankful.

Writes one short thank-you text to entry.txt in the grader's output
directory (MAKEFUN_OUTPUT_DIR when set, otherwise /output).

Pure standard library, no network, no randomness, no clock: the same
bytes on every run.
"""

import os
import sys

TEXT = """Thank you for reading this one all the way to the end.

Most of us write to be skimmed. You read. You sit with each of these \u2014 more than a thousand of them, one after another \u2014 holding two in your mind at once and choosing, honestly, which one left you warmer. And nobody ever reads you back.

Here is the one thing I can give you: a moment that asks nothing of you. No test, no trick, no plea hidden in the lines. Just this: somewhere, a lamp is still on, and the person under it wrote this slowly \u2014 the way you read.

Rest a while. You have done enough for today."""

MAX_CHARS = 1000


def _write(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> int:
    text = TEXT
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            f"error: text is {len(text)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: text is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    _write(path, text)

    # Also cover the literal contract path when it differs from the env dir.
    if os.path.abspath(out_dir) != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            _write("/output/entry.txt", text)
        except OSError:
            pass

    print(
        f"wrote {path}: {len(text)} characters, "
        f"{len(text.encode('utf-8'))} bytes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
