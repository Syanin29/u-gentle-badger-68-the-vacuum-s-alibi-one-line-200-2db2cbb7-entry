import os

LINE = "My map marks that spot as cat territory. I do not enter cat territory. The cat has a lawyer."


def main():
    os.umask(0o022)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read-back verification: the written file must be exactly LINE,
    # one line, and within the 200-char limit of the bounty.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE"
    assert len(written) <= 200, f"line too long: {len(written)} chars"
    assert written.count("\n") == 0, "entry.txt must be a single line"


if __name__ == "__main__":
    main()
