# src/models.py
"""Data models for Ironclad transformations."""
from dataclasses import dataclass
from typing import Any, Dict


# {
#   "content": [
#     {
#       "text": "Basic Starting Document",
#       "color": "black"
#     }
#   ]
# }


@dataclass
class Item:
    """A piece of text with an associated color."""

    text: str
    color: str

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Item":
        """Create an Item from a mapping with 'text' and 'color' keys."""
        return Item(text=d["text"], color=d["color"])
