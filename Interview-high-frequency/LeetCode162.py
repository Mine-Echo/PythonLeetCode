# 寻找峰值
import sys


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # O(n)复杂度解法
        # for i in range(len(nums)):
        #     if i == len(nums) - 1 or nums[i] > nums[i + 1]:
        #         return i

        # O(logn)复杂度解法
        def get(i: int) -> int:
            if -1 < i < len(nums):
                return nums[i]
            return -sys.maxsize - 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return mid
