# 3783. Mirror Distance of an Integer — Easy
# Date: 19.06.2026
# Topic: Math / String
# Time: O(n) | Space: O(n)
# Attempt: 1st try ✓

class Solution(object):
    def mirrorDistance(self, n):
        reversed_str = str(abs(n))[::-1]
        reversed_num = int(reversed_str)

        if n >= reversed_num:
            return n - reversed_num
        else:
            return reversed_num - n
        