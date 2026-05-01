class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp=[]
        for i in range(len(difficulty)):
            dp.append((difficulty[i],profit[i]))

        dp.sort()
        worker.sort()

        profit=0
        print(worker)
        print(dp)
        r =0
        pre = (0,0)
        for w in range(len(worker)):
            for d in range(r,len(dp)):
                cur= dp[d]
                if cur[0] <= worker[w]:
                    if cur[1] > pre[1]:
                        pre = cur
                else:
                    break
            r=d
            profit += pre[1]
            print(profit)
        return profit

        
        