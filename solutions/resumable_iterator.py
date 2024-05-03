# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# implement a resumable iterator with getState()/setState() for list, you can use it in a for loop.
#
################################################


class ResumableIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
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


# Example usage:
my_list = [1, 2, 3, 4, 5]
my_iterator = ResumableIterator(my_list)

# Looping through the list using the iterator
for item in my_iterator:
    print(item)

# Getting and setting state
state = my_iterator.getState()
print("Current state:", state)

# Resetting state
my_iterator.setState(2)  # Resumes from the third element (index 2)
print("Resumed state:", my_iterator.getState())

# Looping again from the resumed state
for item in my_iterator:
    print(item)
