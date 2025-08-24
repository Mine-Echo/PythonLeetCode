import heapq


# 用一个最大堆一个最小堆
class MedianFinder:

    def __init__(self):
        self.cnt = 0
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.cnt == 0:
            heapq.heappush(self.minheap, num)
        elif self.cnt == 1:
            if num > self.minheap[0]:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        elif num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
            # 调整
            if len(self.minheap) - 1 > len(self.maxheap):
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        else:
            heapq.heappush(self.maxheap, -num)
            # 调整
            if len(self.minheap) < len(self.maxheap):
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
        self.cnt += 1

    def findMedian(self) -> float:
        if self.cnt % 2 == 0:
            ret = (self.minheap[0] - self.maxheap[0]) / 2
        else:
            ret = self.minheap[0]
        return ret


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    mf.addNum(3)
    print(mf.findMedian())
