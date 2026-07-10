# 3110. Score of a String — Easy
# Date: 19.06.2026
# Topic: String
# Time: O(n) | Space: O(1)
# Attempt: 1st try ✓

class Solution(object):
    def scoreOfString(self, s):
        total = 0
        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))
        return total