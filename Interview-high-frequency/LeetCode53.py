# 最大子数组和
import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 一遍扫描
        max = -sys.maxsize - 1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            max = sum if sum > max else max
            sum = 0 if sum < 0 else sum
        return max
