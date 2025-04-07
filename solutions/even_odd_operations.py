from typing import Any, Dict, List, Set, Optional


def getMaximumScore(integerArray: List[int]) -> int:
    n = len(integerArray)

    # Precompute prefix sums for quick range sum lookups
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + integerArray[i]

    def get_sum(l, r):
        return prefix_sum[r + 1] - prefix_sum[l]

    # dp[left][right][op_num % 2] will store the result
    dp = [[[None for _ in range(2)] for _ in range(n)] for _ in range(n)]

    def helper(left, right, op_num):
        if left > right:
            return 0

        turn: int = op_num % 2
        if dp[left][right][turn] is not None:
            return dp[left][right][turn]

        current_sum = get_sum(left, right)

        if op_num % 2 == 1:  # odd operation (1-indexed): add sum
            score_left = current_sum + helper(left + 1, right, op_num + 1)
            score_right = current_sum + helper(left, right - 1, op_num + 1)
            dp[left][right][turn] = max(score_left, score_right)
        else:  # even operation: subtract sum
            score_left = -current_sum + helper(left + 1, right, op_num + 1)
            score_right = -current_sum + helper(left, right - 1, op_num + 1)
            dp[left][right][turn] = max(score_left, score_right)

        return dp[left][right][turn]

    return helper(0, n - 1, 1)


# Example usage:
nums = (1, 2, 3, 4, 2, 6)
print(f"input :{nums}, output: {getMaximumScore(nums)}")  # Output: 13

nums = (3, 1, 2, 3)
print(f"input :{nums}, output: {getMaximumScore(nums)}")  # Output: 5
