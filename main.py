"""Write the one-line excuse to the entry file.

Standard library only. Deterministic: the same bytes on every run.
The entry is a single line, 100 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

EXCUSE = (
    "I delegated your deadline to a subagent. "
    "The subagent delegated it back. "
    "We have formed a committee."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
