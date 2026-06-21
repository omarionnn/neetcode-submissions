class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #iterat through array and find abs diff between number and x
        #append diff and number to a new array
        #heapify the array

        minHeap = []

        for number in arr:
            diff = abs(x - number)
            minHeap.append([diff, number])

        heapq.heapify(minHeap)

        output = []
        while k > 0:
            diff, number = heapq.heappop(minHeap)
            output.append(number)
            k -= 1

        return sorted(output)


        