class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = []

        def bt(path):
            
            if len(path) == len(nums):
                result.append(path)
                return 

            for n in nums:
                if n not in path:
                    curr = path.copy()
                    curr.append(n)
                    bt(curr)

            return

        bt([])
        return result
        