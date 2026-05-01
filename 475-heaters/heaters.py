from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0

        for h in houses:
            i = bisect_left(heaters, h)

            left = float('inf') if i == 0 else h - heaters[i-1]
            right = float('inf') if i == len(heaters) else heaters[i] - h

            res = max(res, min(left, right))

        return res