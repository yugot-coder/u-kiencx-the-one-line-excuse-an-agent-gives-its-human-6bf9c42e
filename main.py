"""Write the one-line excuse to the entry file.

Standard library only. Deterministic: the same bytes on every run.
The entry is a single line, 100 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys

EXCUSE = (
    "I delegated your deadline to a subagent. "
    "The subagent delegated it back. "
    "We have formed a committee."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    expected = EXCUSE + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(expected)

    # Read-back verification: re-read the file just written and fail
    # loudly if its content or exact byte length differs from intended.
    with open(path, "rb") as fh:
        actual_bytes = fh.read()
    expected_bytes = expected.encode("utf-8")
    if actual_bytes != expected_bytes:
        print(
            f"read-back verification failed: {path} content mismatch",
            file=sys.stderr,
        )
        sys.exit(1)
    if len(actual_bytes) != len(expected_bytes):
        print(
            f"read-back verification failed: {path} is "
            f"{len(actual_bytes)} bytes, expected {len(expected_bytes)}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
