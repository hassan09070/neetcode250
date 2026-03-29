from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in mp:
                return [mp[complement], i]

            mp[num] = i