# 查找最小的K对数字

import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: list[int], nums2: list[int], k: int
    ) -> list[list[int]]:
        # 暴力用堆，超出内存限制
        # heap = []
        # for i in range(min(len(nums1), k)):
        #     for j in range(min(len(nums2), k)):
        #         heapq.heappush(heap, (nums1[i] + nums2[j], nums1[i], nums2[j]))
        # result = []
        # while k > 0:
        #     num = heapq.heappop(heap)
        #     result.append([num[1], num[2]])
        #     k -= 1
        # return result

        heap = []
        hashset = set()
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        result = []
        while k > 0:
            (_, i, j) = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            # 核心思想，当(i,j)出栈时，需要将(i+1,j)和(i,j+1)入栈
            if (i + 1, j) not in hashset and i < len(nums1) - 1:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                hashset.add((i + 1, j))
            if (i, j + 1) not in hashset and j < len(nums2) - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                hashset.add((i, j + 1))
            k -= 1
        return result
