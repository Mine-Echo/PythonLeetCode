# 环形子数组的最大和
import sys


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # 反向思维：跨越边界的情况通过nums_sum-min求
        max_sum = -sys.maxsize - 1
        min_sum = sys.maxsize
        nums_sum = 0
        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            nums_sum += nums[i]
            sum1 += nums[i]
            sum2 += nums[i]
            max_sum = max(sum1, max_sum)
            min_sum = min(sum2, min_sum)
            if sum1 < 0:
                sum1 = 0
            if sum2 > 0:
                sum2 = 0
        # 数组全为负数的特殊情况，此时nums_sum-min=0，应该返回小于0的max
        if max_sum < 0:
            return max_sum
        return max(nums_sum - min_sum, max_sum)


if __name__ == "__main__":
    list = [5, -3, 5]
    Solution().maxSubarraySumCircular(list)
