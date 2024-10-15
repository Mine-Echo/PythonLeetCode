# 寻找旋转排序数组中的最小值


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (
                mid == len(nums) - 1 or nums[mid] > nums[mid + 1]
            ):
                return nums[mid]
            elif nums[mid] <= nums[len(nums) - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
