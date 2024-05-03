# -*- coding: utf-8 -*-

################################################
#
# openai coding question
#
# 实现一个MultipleResumableFileIterator with existing ResumableFileIterator to iterator multiple json file.
# Be able to handle empty file case
#
################################################
import json

class ResumableFileIterator:
    def __init__(self, filename):
        self.filename = filename
        self.index = 0
        self.data = self.load_data()

    def load_data(self):
        with open(self.filename, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # Handle empty file case
        return data

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

    def setState(self, state):
        if 0 <= state < len(self.data):
            self.index = state
        else:
            raise ValueError("Invalid state value")


class MultipleResumableFileIterator:
    def __init__(self, filenames):
        self.filenames = filenames
        self.current_file_index = 0
        self.current_iterator = None
        self.load_next_file()

    def load_next_file(self):
        if self.current_file_index < len(self.filenames):
            self.current_iterator = ResumableFileIterator(self.filenames[self.current_file_index])
            self.current_file_index += 1
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iterator)
        except StopIteration:
            self.load_next_file()
            return next(self.current_iterator)

    def getState(self):
        return self.current_file_index - 1, self.current_iterator.getState()

    def setState(self, state):
        file_index, iterator_state = state
        if 0 <= file_index < len(self.filenames):
            self.current_file_index = file_index + 1
            self.current_iterator = ResumableFileIterator(self.filenames[file_index])
            self.current_iterator.setState(iterator_state)
        else:
            raise ValueError("Invalid file index")


# Example usage:
filenames = ["file1.json", "file2.json", "empty_file.json", "file3.json"]
multi_iterator = MultipleResumableFileIterator(filenames)

for item in multi_iterator:
    print(item)

# Getting and setting state
state = multi_iterator.getState()
print("Current state:", state)

# Resetting state
multi_iterator.setState(state)
print("Resumed state:", multi_iterator.getState())