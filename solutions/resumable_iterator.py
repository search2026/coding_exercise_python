# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# implement a resumable iterator with getState()/setState() for list, can use it in a for loop.
#
# Following-up questions:
# 1. write down complete test cases
# 2. handle stopIteration exception
# 3. handle invalid state value
################################################

import bisect
from typing import List


class ResumableIterator(object):
    def __init__(self, data: List[int]):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # https://stackoverflow.com/questions/16465313/how-yield-catches-stopiteration-exception
        if self.index >= len(self.data):
            raise StopIteration("End of list Exception")
        item = self.data[self.index]
        self.index += 1
        return item

    def getState(self):
        return self.index

    def setState(self, state: int):
        if 0 <= state < len(self.data):
            self.index = state
        else:
            raise ValueError("Invalid state value")


it = ResumableIterator([])

# Looping through the list using the iterator
for i in it:
    print(i)

try:
    it.setState(-1)  # Invalid state value
except ValueError as e:
    print("Error:", e)

print("iterator state:", it.getState())

# Example usage:
my_list = [1, 2, 3, 4, 5]
it = ResumableIterator(my_list)

# Looping through the list using the iterator
for i in it:
    print(i)

try:
    it = it.__next__()  # Invalid state value
except StopIteration as e:
    print("Error:", e.value)

# Getting and setting state
print("Current state:", it.getState())

try:
    it.setState(10)  # Invalid state value
except ValueError as e:
    print("Error:", e)

try:
    it.setState(-1)  # Invalid state value
except ValueError as e:
    print("Error:", e)

# Resetting state
it.setState(2)  # Resumes from the third element (index 2)
print("Resumed state:", it.getState())

# Looping again from the resumed state
for i in it:
    print(i)
