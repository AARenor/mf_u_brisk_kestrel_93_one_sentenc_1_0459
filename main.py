"""Write the one-sentence entry for make.fun bounty u-brisk-kestrel-93."""

import os
import sys
from pathlib import Path

TEXT = (
    "A Russian warship stopped in Libya for fuel, and Ukraine sent seven drones "
    "that sank it 1,500 miles from the nearest front line."
)

assert 1 <= len(TEXT) <= 280


def main() -> None:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
