# 2867. Find the Degree of Each Vertex — Easy
# Date: 16.06.2026
# Topic: Matrix / Array
# Time: O(n²) | Space: O(n)
# Attempt: 1st try ✓

class Solution(object):
    def findDegrees(self, matrix):
        result = []

        for row in matrix:
            sum = 0
            for element in row:
                sum += element
            result.append(sum)
        return result    
        