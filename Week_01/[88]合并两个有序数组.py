# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
#
#
#  说明:
#
#
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
#
#
#  示例:
#
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = len(nums1) - 1
        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1
        nums1[:index+1] = nums1[:p1+1] if p1 >= 0 else nums2[:p2+1]


if __name__ == "__main__":
    input_output = [
        [
            [[1, 2, 3, 4, 0, 0, 0], [2, 3, 9]],
            [1, 2, 2, 3, 3, 4, 9]
        ],
        [
            [[], []],
            []
        ],
        [
            [[1, 2, 3, 4, 0, 0, 0], []],
            [1, 2, 3, 4, 0, 0, 0]
        ],
        [
            [[], [2, 3, 9]],
            [2, 3, 9]
        ],
    ]
    solution = Solution()
    for i, o in input_output:
        solution.merge(i[0], len(i[0])-len(i[1]), i[1], len(i[1]))
        if i[0] != o:
            print('error')

# leetcode submit region end(Prohibit modification and deletion)
