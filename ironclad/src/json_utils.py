import json
from pathlib import Path
from models import Item


def load_json(path: Path | str):
    """Load and parse a JSON file from the given path."""
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path | str, data):
    """Write JSON data to the given path with pretty formatting."""
    path = Path(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_items(path: Path | str):
    """Load a JSON file containing a "content" list into a list of Items."""
    raw = load_json(path)
    return [Item.from_dict(d) for d in raw["content"]]
