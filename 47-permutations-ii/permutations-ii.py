
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        def bt(path, used):
            if len(path) == len(nums):
                results.append(path.copy())
                return

            for x in range(len(nums)):
                if used[x]:
                    continue

                # Skip duplicate choices at this recursion level
                if x > 0 and nums[x] == nums[x - 1] and not used[x - 1]:
                    continue

                path.append(nums[x])
                used[x] = True

                bt(path, used)

                used[x] = False
                path.pop()

        bt([], [False] * len(nums))
        return results