class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #go through points and compute distance
        #heapify the array
        #pop until there 
        minHeap = []
        res = []

        for x, y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res