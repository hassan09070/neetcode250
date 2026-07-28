from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only one house
        if len(nums) == 1:
            return nums[0]

        # Standard House Robber (linear)
        def robLine(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Exclude the last house
        # Case 2: Exclude the first house
        return max(
            robLine(nums[:-1]),
            robLine(nums[1:])
        )