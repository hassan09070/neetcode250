from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])  # copy
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])          # choose
                backtrack(i, path, target - candidates[i])  # reuse allowed
                path.pop()                          # undo

        backtrack(0, [], target)
        return res