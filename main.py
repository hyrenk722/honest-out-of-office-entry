"""The Painfully Honest Out-of-Office — make.fun entry.

Competition: u-po-pu-the-painfully-honest-out-of-office-63e7ca0b
The program writes one out-of-office auto-reply, a single sentence of
1 to 200 UTF-8 characters, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
import sys

ENTRY_TEXT = (
    "I'm away until Monday, and yes, I can see your email from the beach "
    "— I'll answer it properly when I'm back, once I've finished "
    "pretending I'm not working."
)


def check_gate(text):
    """Return True only if the text passes the competition gate."""
    if not text or not text.strip():
        return False
    encoded = text.encode("utf-8")
    if len(encoded) < 1 or len(encoded) > 200:
        return False
    return True


def main():
    if not check_gate(ENTRY_TEXT):
        print("gate failed: entry must be 1 to 200 UTF-8 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != ENTRY_TEXT.encode("utf-8"):
        print("verify failed: written bytes do not match entry", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (out_path, len(written)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
