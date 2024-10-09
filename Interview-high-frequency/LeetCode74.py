# 搜索二维矩阵


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 二分查找
        num_row, num_column = len(matrix), len(matrix[0])
        left, right = 0, num_column * num_row - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // num_column][mid % num_column] < target:
                left = mid + 1
            elif matrix[mid // num_column][mid % num_column] > target:
                right = mid - 1
            else:
                return True
        return False
