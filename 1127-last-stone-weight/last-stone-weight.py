class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) >1:
            y = stones[-1]
            x = stones[-2]

            if x==y:
                stones = stones[:-2]
            else:
                stones = stones[:-2]
                stones.append(y-x)
                stones.sort()

        return stones[0] if len(stones) >0 else 0
        