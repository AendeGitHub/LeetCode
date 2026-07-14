# 3512. Minimum Operations to Make Array Sum Divisible by K — Easy
# Date: 16.07.2026
# Topic: Math / Array
# Time: O(n) | Space: O(1)
# Attempt: 1st try ✓

class Solution(object):
    def minOperations(self, nums, k):
        sum = 0
        for i in nums:
            sum += i
        return sum%k
        