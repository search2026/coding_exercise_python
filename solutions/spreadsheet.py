# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# given a cell class
# class Cell {    Integer value;    String child1;    String child2;     public Cell(Integer value, String child1, String child2) {      this.value = value;      this.child1 = child1;      this.child2 = child2;   } }
# Integer value;    String child1;    String child2;
# public Cell(Integer value, String child1, String child2)
# {      this.value = value;      this.child1 = child1;      this.child2 = child2;   } }
#
# #Write two function getCell() and SetCellValue()
#
# example:
# Cell A = Cell (6, NULL, NULL)
# Cell B = Cell (7, NULL, NULL)
# Cell C = Cell (13, A, B)
# print getCell(C) ====> 13
# A+B = 6+7 = 13
# update Cell A = Cell (2, NULL, NULL)
# print getCell(C) => 9
# A+B = 2+7 = 9
################################################

from typing import Dict, Set, Optional

# TODO: add tests
# TODO: add caching


cell_dict: Dict[str, 'Cell'] = {}

class Cell:
    def __init__(self, value=None, child1=None, child2=None):
        self.value = value
        if value:
            assert child1 == child2 is None
        if child1 or child2:
            assert value is None
        self.child1 = child1
        self.child2 = child2
        self.parents: Set['Cell'] = set()

    def get_value(self) -> int:
        if self.value:
            return self.value
        if self.child1 not in cell_dict or self.child2 not in cell_dict:
            raise ValueError(f"fail to find children c1: {self.child1} c2: {self.child2}")
        v = cell_dict[self.child1].get_value() + cell_dict[self.child2].get_value()
        self.value = v
        return v

    def set_parent(self, parent: 'Cell', visited: Optional[Set] = None):
        if not visited:
            visited = set()
        if parent in visited:
            raise ValueError("Circular dependency detected")
        visited.add(parent)
        self.parents.add(parent)
        if self.child1 and self.child2:
            cell_dict[self.child1].set_parent(self, visited)
            cell_dict[self.child2].set_parent(self, visited)

    def invalidate(self):
        self.value = None
        for parent in self.parents:
            parent.invalidate()


class SpreadSheet:
    def get_cell_value(self, key: str):
        return cell_dict[key].get_value()

    def set_cell(self, key: str, cell: Cell):
        if key in cell_dict:
            cell_dict[key].invalidate()
        cell_dict[key] = cell
        if cell.child1 and cell.child2:
            cell_dict[cell.child1].set_parent(cell)
            cell_dict[cell.child2].set_parent(cell)


def __main__():
    spreadsheet = SpreadSheet()
    spreadsheet.set_cell("A", Cell(6))
    spreadsheet.set_cell("B", Cell(7))
    spreadsheet.set_cell("C", Cell(value=None, child1="A", child2="B"))
    assert spreadsheet.get_cell_value("C") == 13
    spreadsheet.set_cell("A", Cell(5))
    assert spreadsheet.get_cell_value("C") == 12
    spreadsheet.set_cell("D", Cell(10))
    spreadsheet.set_cell("E", Cell(15))
    spreadsheet.set_cell("F", Cell(value=None, child1="D", child2="E"))
    assert spreadsheet.get_cell_value("F") == 25, "Incorrect value for cell F"
    spreadsheet.set_cell("D", Cell(20))
    assert spreadsheet.get_cell_value("F") == 35, "Incorrect value for cell F after updating value of D"
    # Test 2: Test circular dependency detection
    try:
        spreadsheet.set_cell("D", Cell(value=None, child1="F", child2="E"))
    except ValueError as e:
        assert str(e) == "Circular dependency detected"
    else:
        raise AssertionError("Circular dependency not detected as expected")


__main__()

# set_cell("C1", "45")
# set_cell("B1", "10")
# set_cell("A1", "= C1+B1")
# get_cell("A1")  # should return 55 in this case
