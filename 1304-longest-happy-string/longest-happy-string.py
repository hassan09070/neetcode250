import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        arr = []
        for count, ch in [(a,'a'), (b,'b'), (c,'c')]:
            if count > 0:
                heapq.heappush(arr, (-count, ch))

        s = ""

        while arr:
            count1, ch1 = heapq.heappop(arr)

            # if adding ch1 makes 3 consecutive
            if len(s) >= 2 and s[-1] == s[-2] == ch1:
                if not arr:
                    break

                count2, ch2 = heapq.heappop(arr)

                s += ch2
                count2 += 1   # since negative

                if count2 < 0:
                    heapq.heappush(arr, (count2, ch2))

                heapq.heappush(arr, (count1, ch1))

            else:
                s += ch1
                count1 += 1

                if count1 < 0:
                    heapq.heappush(arr, (count1, ch1))

        return s