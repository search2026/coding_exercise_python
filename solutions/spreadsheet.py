# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# given a Cell class
#
# public class Cell {
#   Integer value;
#   String child1;
#   String child2;
#
#   public Cell(Integer value, String child1, String child2)
#   {
#       this.value = value;
#       this.child1 = child1;
#       this.child2 = child2;
#   }
# }

# Implement two functions called getCell() and SetCellValue()
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

# Following-up questions:
# 1. How to handle cyclic dependency?
# 2. Improve performance add caching?
################################################

from typing import Dict, Set, Optional


class Cell:
    def __init__(self, value, child1=None, child2=None):
        self.value = value
        if value:
            assert child1 == child2 is None
        if child1 or child2:
            assert value is None
        self.child1 = child1
        self.child2 = child2
        self.cache = {}

    def get_value(self, visited=set()):
        if visited is None:
            visited = set()
        if isinstance(self.value, int):
            return self.value
        else:
            if id(self) in visited:
                raise ValueError("Cyclic dependency detected")

            if id(self) in self.cache:
                return self.cache[id(self)]

            visited.add(id(self))
            cell_value = self.child1.get_value(visited) + self.child2.get_value(visited)
            self.cache[id(self)] = cell_value
            visited.remove(id(self))

            return cell_value

    def set_value(self, value):
        self.value = value
        self.invalidate_cache()

    def invalidate_cache(self):
        if id(self) in self.cache:
            del self.cache[id(self)]

        if isinstance(self.value, int):
            return
        else:
            self.child1.invalidate_cache(self.cache)
            self.child2.invalidate_cache(self.cache)


# Example usage:
A = Cell(6)
B = Cell(7)
C = Cell(13, A, B)

print("Initial value of cell C:", C.get_value())  # Output: 13

# Update value of cell A
A.set_value(2)

print("Updated value of cell C:", C.get_value())  # Output: 9

# Creating a cyclic dependency
A.child1 = C

try:
    print("Value of cell A:", A.get_value())  # Output: Raises ValueError
except ValueError as e:
    print("Error:", e)
