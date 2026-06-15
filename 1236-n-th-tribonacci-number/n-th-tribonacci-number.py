class Solution:
    def tribonacci(self, n: int) -> int:
        dit = {
            0:0,
            1:1,
            2:1
        }

        for i in range(3,n+1):
            dit[i]= dit [i-1] + dit[i-2]+dit[i-3]


        return dit[n]
        