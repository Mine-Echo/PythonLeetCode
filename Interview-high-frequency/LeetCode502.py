# IPO
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: list[int], capital: list[int]
    ) -> int:
        n = len(profits)
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x: x[0])
        index = 0

        heap = []
        for _ in range(k):
            while index < n and arr[index][0] <= w:
                heapq.heappush(heap, arr[index][1])
                index += 1
            if heap:
                w += heapq.heappop(heap)
            else:
                break

        return w
