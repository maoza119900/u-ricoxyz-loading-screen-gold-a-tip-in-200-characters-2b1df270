"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip for stressed developers and AI
coding agents to entry.txt in the output directory.

Fully deterministic: no time, no randomness, no network, no file
traversal. The tip is a fixed string constant.
"""

import os

TIP = (
    "Tip: stretch while this loads \u2014 your AI just rewrote "
    "your function, broke the tests, and is now confidently "
    "explaining why that was your idea."
)


def main() -> None:
    # Guard the gate at runtime: one line, 1-200 characters, non-blank.
    assert 1 <= len(TIP) <= 200 and TIP.strip() and "\n" not in TIP
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
