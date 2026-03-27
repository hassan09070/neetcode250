class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if amount in mem:
                return mem[amount]

            minn = float('inf')

            for c in coins:
                res = dp(amount - c)
                if res != -1:
                    minn = min(minn, 1 + res)

            mem[amount] = -1 if minn == float('inf') else minn
            return mem[amount]

        return dp(amount)