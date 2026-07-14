# Convert the Temperature - Easy
# Date: 13.07.2026
# Topic: Math
# Time: O(1) | Space: O(1)
# Attempt: 1st try ✓

class Solution(object):
    def convertTemperature(self, celsius):
        return [celsius + 273.15, celsius * 1.8 + 32]