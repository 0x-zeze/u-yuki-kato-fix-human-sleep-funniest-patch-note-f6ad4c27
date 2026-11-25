from pathlib import Path

ENTRY = (
    "Fixed: Sleeping a full 8 hours no longer leaves users groggier than a 2-hour nap; "
    "widened rest_hours from uint3 to uint8 so 8 stops wrapping to 0."
)
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(f"{ENTRY}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
