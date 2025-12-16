# src/transform.py
"""Text transformation utilities for applying multi-item text edits."""
from typing import Any, Dict, List
import logging
from models import Item

logger = logging.getLogger(__name__)


def apply_edits(
    items: List[Item],
    edit_op: Dict[str, Any],
) -> List[Item]:
    """Apply a single edit operation to a list of Items.

    The selection may span multiple items. The replacement is inserted at the
    selection start after deletions (if any).

    Args:
        items: The input list of Items.
        edit_op: A mapping with keys 'selection' (startIndex, length) and 'replacement'.

    Returns:
        A new list of Items reflecting the edit.
    """
    result = list(items)
    # there is only one edit command at one call
    # assume edit json is always in valid format
    # sampole edit_op:
    # {
    # "selection": {
    #     "startIndex": 6,
    #     "length": 0
    # },
    # "replacement": "Inserted "
    # }

    start_index = edit_op["selection"]["startIndex"]
    delete_length = edit_op["selection"]["length"]
    insert_str = edit_op["replacement"]

    # We'll compute two things while scanning items:
    # - insert_item: which item the original start_index falls into
    # - insert_offset: the character offset inside that item where insertion happens
    # Also collect deletion operations spanning multiple items.
    item_del_ops: List = []  # (item_index, del_start, del_len)
    insert_item: int = -1
    insert_offset: int = 0

    # Keep separate counters so we don't lose the original insertion offset
    remaining_start = start_index
    remaining_delete = delete_length

    for i, item in enumerate(result):
        item_length = len(item.text)

        if insert_item == -1:
            if remaining_start <= item_length:
                insert_item = i
                insert_offset = remaining_start
            else:
                remaining_start -= item_length

        if remaining_delete > 0:
            # The deletion starts at insert_item/insert_offset; for items before insert_item, nothing to delete
            if insert_item == -1:
                # Haven't reached the start yet; nothing to delete in this item
                continue

            # Determine start of deletion within this item
            if i == insert_item:
                del_start = insert_offset
                available = max(0, item_length - del_start)
            else:
                del_start = 0
                available = item_length

            if available > 0:
                del_len = min(remaining_delete, available)
                if del_len > 0:
                    item_del_ops.append((i, del_start, del_len))
                    remaining_delete -= del_len

        # If both found and no more deletion needed, we can stop early
        if insert_item != -1 and remaining_delete <= 0 and remaining_start <= 0:
            # We already know insertion spot and finished deletions
            # But we still need to continue when remaining_start > 0 (shouldn't happen once insert_item set)
            pass

    logger.debug(
        "item_del_ops=%s insert_item=%s insert_offset=%s",
        item_del_ops,
        insert_item,
        insert_offset,
    )

    # Apply deletions from last to first to keep indices valid
    item_to_be_deleted: List = []
    for item_num, del_start, del_length in reversed(item_del_ops):
        item = result[item_num]
        item.text = item.text[:del_start] + item.text[del_start + del_length :]
        if len(item.text) == 0:
            item_to_be_deleted.append(item_num)

    logger.debug("item_to_be_deleted=%s", item_to_be_deleted)

    # Perform insertion at the computed offset in the correct item
    if insert_item >= 0 and insert_str:
        original_text = result[insert_item].text
        result[insert_item].text = (
            original_text[:insert_offset] + insert_str + original_text[insert_offset:]
        )
        logger.debug(
            "after insertion item=%s text=%s", insert_item, result[insert_item].text
        )

    # Merge adjacent items with same color when deletions create empty boundaries;
    # also drop empty items
    for item_num in sorted(set(item_to_be_deleted), reverse=True):
        del result[item_num]

    return result
