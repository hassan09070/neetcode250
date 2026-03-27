class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            rob = nums[i] + dp(i - 2)
            skip = dp(i - 1)

            memo[i] = max(rob, skip)
            return memo[i]

        return dp(len(nums) - 1)