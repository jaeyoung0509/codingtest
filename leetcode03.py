'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
Given a string s, find the length of the longest substring without repeating characters.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlen = 0
        lookup ={}
        for idx ,char in enumerate(s):
            if char in lookup and start <= lookup[char]:
                start = lookup[char]+1
            else:
                maxlen = max(maxlen , idx - start + 1)
            lookup[char] = idx
        return maxlen