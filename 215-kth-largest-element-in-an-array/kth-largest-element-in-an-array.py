import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)   # build min heap

        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappushpop(heap, n)

        return heap[0]