from pathlib import Path

LINE = "My agent proudly shrank my 4K wedding video from 8 GB to 3 MB — by converting it to MP3."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
