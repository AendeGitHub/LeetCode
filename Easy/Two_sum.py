# 001. Two Sum - Easy
# Date: 03.06.2026
# Topic: Brute Force
# Time: O(n²) | Space: O(1)
# Attempt: 1st try ✓

class Solution(object):
    def twoSum(self, nums, target):
        nums_len = len(nums)

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                s = nums[i] + nums[j]
                if s == target:
                    return([i, j])
        