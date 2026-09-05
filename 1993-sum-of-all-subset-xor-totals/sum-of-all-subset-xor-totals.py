class Solution:
    def subsetXORSum(self, nums):
        def dfs(i, curr_xor):
            if i == len(nums):
                return curr_xor
            
            # include nums[i]
            include = dfs(i + 1, curr_xor ^ nums[i])
            
            # exclude nums[i]
            exclude = dfs(i + 1, curr_xor)
            
            return include + exclude
        
        return dfs(0, 0)