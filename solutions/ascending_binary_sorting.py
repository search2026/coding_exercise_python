from typing import Any, Dict, List, Set, Optional


def sort_by_ones_binary(numbers: List[int]) -> List[int]:
    # Sort by the number of 1's in the binary representation, then by the decimal value
    return sorted(numbers, key=lambda x: (bin(x).count('1'), x))

# Example usage
nums = (7, 8, 6, 5)
print(f"input :{nums}, output: {sort_by_ones_binary(nums)}")    # Output: [8, 5, 6, 7]

nums = (1, 2, 3)
print(f"input :{nums}, output: {sort_by_ones_binary(nums)}")    # Output: [1, 2, 3]
