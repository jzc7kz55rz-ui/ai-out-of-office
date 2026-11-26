import os

ENTRY = 'I am on vacation. Your email has been queued for my return, right behind the 4,000 emails I ignored before I left.'
MAX_CHARS = 160  # the gate accepts 1..160 characters


def entry_text():
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, "entry must fit the gate"
    return text


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry_text())


if __name__ == "__main__":
    main()
