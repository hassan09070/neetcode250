
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        def bt(path, i):
            results.append(path.copy())

            for x in range(i, len(nums)):
                if x > i and nums[x] == nums[x - 1]:
                    continue

                path.append(nums[x])
                bt(path, x + 1)
                path.pop()

        bt([], 0)
        return results