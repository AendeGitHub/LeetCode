# 3668. Restore Finishing Order — Easy
# Date: 19.06.2026
# Topic: Array / Hash Map
# Time: O(n²) | Space: O(n)
# Attempt: 1st try ✓

class Solution(object):
    def recoverOrder(self, order, friends):
        result = []
        for i in order:
            for j in friends:
                if i == j:
                    result.append(i)
        return result

# Optimized — O(n) | Space: O(n)
# friends_set = set(friends)
# return [i for i in order if i in friends_set]