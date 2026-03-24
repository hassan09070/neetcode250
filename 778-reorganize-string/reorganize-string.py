import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        
        # Count frequency
        for char in s:
            freq[char] = 1 + freq.get(char, 0)

        # Build max heap
        heap = []
        for k, v in freq.items():
            heap.append((-v, k))   # negative for max heap
        
        heapq.heapify(heap)

        prev = None
        result = []

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            # push previous back if exists
            if prev:
                heapq.heappush(heap, prev)
                prev = None

            # decrease count
            if count + 1 < 0:
                prev = (count + 1, char)

        result = "".join(result)

        # check validity
        if len(result) != len(s):
            return ""

        return result