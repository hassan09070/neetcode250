class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sort = []
        heapq.heapify(sort)
        for t in trips:
            heapq.heappush(sort,(t[1],t[2],t[0]))

        car = []
        heapq.heapify(car)
        people = 0
        loc = 0
        for i in range(len(trips)):
            trip = heapq.heappop(sort)
            t= [trip[2],trip[0],trip[1]]
            loc = t[1]

            while car and car[0][0] <= loc:
                people -= car[0][1]
                heapq.heappop(car)

            if people+t[0] > capacity :
                return False
            
            people += t[0]
            heapq.heappush(car, (t[2],t[0]))


        return True

                



        