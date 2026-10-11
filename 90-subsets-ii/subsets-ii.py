class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        results=[]
        nums.sort()

        def bt(path,i):
            if path not in results:
                results.append(path.copy())
            if i == len(nums):
                return 

            for x in range(i,len(nums)):
                cur= path.copy()
                cur.append(nums[x])
                bt(cur,x+1)

        bt([],0)
        return results
        