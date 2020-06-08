# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in cache:
                return [cache[need], i]
            cache[nums[i]] = i
        return []


if __name__ == "__main__":
    input_output = [
        [
            [
                [0, 3, -1, 4, 6, 8],
                3
            ],
            [0, 1]
        ],
        [
            [
                [5, 3, -1, 4, 6, 8],
                2
            ],
            [1, 2]
        ],
        [
            [
                [5, 3, -1, 4, 6, 8],
                3
            ],
            [2, 3]
        ],
        [
            [
                [5, 3, -1, 4, 6, 8],
                200
            ],
            []
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        res = solution.twoSum(*i)
        if res != o:
            print('error')
# leetcode submit region end(Prohibit modification and deletion)
