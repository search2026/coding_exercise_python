import json
from pathlib import Path
import logging

from ironclad.src.json_utils import load_items, load_json
from ironclad.src.transform import apply_edits


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "test-cases"


def _run_case(case_dir: Path):
    before = load_items(case_dir / "before.json")
    edit = load_json(case_dir / "edit.json")
    expected = load_items(case_dir / "result.json")

    actual = apply_edits(before, edit)
    assert actual == expected


def test_01_single_node_insert():
    _run_case(DATA_DIR / "01-single-node-insert")


def test_02_single_node_replace():
    _run_case(DATA_DIR / "02-single-node-replace")


def test_03_single_node_append():
    _run_case(DATA_DIR / "03-single-node-append")


def test_04_single_node_replace_start():
    _run_case(DATA_DIR / "04-single-node-replace-start")


def test_05_multi_node_insert():
    _run_case(DATA_DIR / "05-multi-node-insert")


def test_06_multi_node_in_between():
    _run_case(DATA_DIR / "06-multi-node-in-between")


def test_07_choose_node():
    _run_case(DATA_DIR / "07-choose-node")


def test_08_spanning_replacement():
    _run_case(DATA_DIR / "08-spanning-replacement")


def test_09_multi_spanning_replacement():
    _run_case(DATA_DIR / "09-multi-spanning-replacement")


def test_10_complex_spanning():
    _run_case(DATA_DIR / "10-complex-spanning")


def test_11_complex_spanning_2():
    _run_case(DATA_DIR / "11-complex-spanning-2")
