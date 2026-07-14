# 3925. Concatenate Array With Reverse — Easy
# Date: 17.06.2026
# Topic: Array
# Time: O(n) | Space: O(1)
# Attempt: 1st try ✓

class Solution(object):
    def concatWithReverse(self, nums):
        nums1 = len(nums)
        for i in range(len(nums)):
            nums.append(nums[nums1 - 1 - i])
        return nums