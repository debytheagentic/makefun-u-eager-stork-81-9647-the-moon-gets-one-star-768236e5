import os

ENTRY = "1 star. Watches me through the window all night and never blinks."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    n = len(ENTRY)
    print("LEN=%d" % n)
    if not ENTRY.strip() or not (1 <= n <= 120):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
