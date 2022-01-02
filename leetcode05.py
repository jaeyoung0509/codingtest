'''
https://leetcode.com/problems/longest-palindromic-substring/Given a string s, find the length of the longest substring without repeating characters.
Given a string s, return the longest palindromic substring in s
https://velog.io/@jaeyoung0509/Leetcode-5.-Longest-Palindromic-Substring
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindromic(s):
            if s == s[::-1]:return True
        for i in range(len(s),0  ,-1):
            for j in range(0 , len(s) - i +1):
                if check_palindromic(s[j: i+j]):
                    return s[j: i+j]
        