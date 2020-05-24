# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
#  示例:
#
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#  说明:
#
#
#  必须在原数组上操作，不能拷贝额外的数组。
#  尽量减少操作次数。
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        store_index = 0
        for i, v in enumerate(nums):
            if v != 0:
                if i != store_index:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1


if __name__ == "__main__":
    input_output = [
        [
            [1, 2, 0, 9, 2, 1, -5, 0, 6],
            [1, 2,  9, 2, 1, -5, 6, 0, 0],
        ],
        [
            [],
            []
        ],
        [
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [1, 2, 3],
            [1, 2, 3]
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        solution.moveZeroes(i)
        if i != o:
            print('error')
# leetcode submit region end(Prohibit modification and deletion)
