import logging
import os
import argparse
from pathlib import Path
from json_utils import load_items, load_json, save_json
from transform import apply_edits

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "test-cases"


def main():
    test_dirs = [
        DATA_DIR / "01-single-node-insert",
        DATA_DIR / "02-single-node-replace",
        DATA_DIR / "03-single-node-append",
        DATA_DIR / "04-single-node-replace-start",
        DATA_DIR / "05-multi-node-insert",
        DATA_DIR / "06-multi-node-in-between",
        DATA_DIR / "07-choose-node",
        DATA_DIR / "08-spanning-replacement",
        DATA_DIR / "09-multi-spanning-replacement",
        DATA_DIR / "10-complex-spanning",
        DATA_DIR / "11-complex-spanning-2",
    ]

    for test_dir in test_dirs:
        logger.info("start edit for %s...", test_dir)

        # assume test files are well formed
        before_json = test_dir / "before.json"
        edit_op_json = test_dir / "edit.json"
        after_json = test_dir / "result.json"

        # load test data
        before_edit_items = load_items(before_json)
        logger.debug("items: %s", before_edit_items)
        edit_op = load_json(edit_op_json)
        logger.debug("edit_op: %s", edit_op)
        expectedc_edited_items = load_items(after_json)
        logger.debug("expected_items: %s", expectedc_edited_items)

        # apply edits
        actual_output_items = apply_edits(before_edit_items, edit_op)
        logger.debug("actual_output_items: %s", actual_output_items)

        # verify the result
        assert actual_output_items == expectedc_edited_items

        logger.info("edit is complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Ironclad edit test harness")
    parser.add_argument(
        "--log-level",
        default=(os.getenv("IRONCLAD_LOG_LEVEL") or "INFO"),
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
        help="Logging level (default from IRONCLAD_LOG_LEVEL env var or INFO)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log_level.upper()))
    main()
