# 009. Palindrome Number — Easy
# Date: 03.06.2026
# Topic: String / Two Pointers
# Time: O(n) | Space: O(n)
# Attempt: 1st try ✓

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        return s == s[::-1]