class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []

        # store index and distance
        for i, v in enumerate(points):
            distance = v[0]**2 + v[1]**2  # no need for sqrt
            lst.append((i, distance))

        # sort by distance
        lst.sort(key=lambda x: x[1])

        # pick first k points
        output = []
        for i in range(k):
            index = lst[i][0]
            output.append(points[index])

        return output