# 搜索旋转排序数组
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # 把所有情况都考虑进去
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # nums[mid]>target的三种情况
            elif nums[mid] > target >= nums[0]:
                right = mid - 1
            elif nums[mid] >= nums[0] > target:
                left = mid + 1
            elif nums[0] > nums[mid] > target:
                right = mid - 1
            # nums[mid]<target的三种情况
            elif nums[mid] < target < nums[0]:
                left = mid + 1
            elif nums[0] <= nums[mid] < target:
                left = mid + 1
            elif nums[mid] < nums[0] <= target:
                right = mid - 1
        return -1
        # 还有一种方法，先二分查找找出旋转点，再进行查找
