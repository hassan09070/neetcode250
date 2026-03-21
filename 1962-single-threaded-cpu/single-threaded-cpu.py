import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # add index
        tasks = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        tasks.sort()  # sort by enqueue time
        
        heap = []
        order = []
        clock = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            # if no task available → jump time
            if not heap and clock < tasks[i][0]:
                clock = tasks[i][0]

            # push all available tasks into heap
            while i < n and tasks[i][0] <= clock:
                et, pt, idx = tasks[i]
                heapq.heappush(heap, (pt, idx))
                i += 1

            # process one task
            pt, idx = heapq.heappop(heap)
            clock += pt
            order.append(idx)

        return order