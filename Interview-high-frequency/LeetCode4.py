# 寻找两个正序数组的中位数


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 先merge再取中位数
        merge = []
        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                merge.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                merge.append(nums1[i])
                i += 1
            else:  # 两个数组都还有元素
                if nums1[i] < nums2[j]:
                    merge.append(nums1[i])
                    i += 1
                else:
                    merge.append(nums2[j])
                    j += 1
        l = len(merge)
        return (merge[l // 2] + merge[l // 2 - 1]) / 2 if l % 2 == 0 else merge[l // 2]
