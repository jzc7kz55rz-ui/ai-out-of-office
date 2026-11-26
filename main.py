import os

ENTRY = "I am on vacation. Your email has been queued for my return, right behind the 4,000 emails I ignored before I left."
MAX_CHARS = 160


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        out_path = "entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
