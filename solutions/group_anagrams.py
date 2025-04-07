# Group Anagrams
import collections


# Given an array of strings, write a function which would group the anagrams together.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#
# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# All inputs will be in lowercase.


class Solution:
    # Time: O(n * k)
    # Space: O(n * k)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()


inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(inputs))
