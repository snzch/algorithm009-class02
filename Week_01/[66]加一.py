# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
#  你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  示例 1:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
#  示例 2:
#
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    input_output = [
        [
            [9, 9, 9, 9],
            [1, 0, 0, 0, 0]
        ],
        [
            [1],
            [2]
        ],
        [
            [1, 3],
            [1, 4]
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        r = solution.plusOne(i)
        if r != o:
            print('error', r, o)

# leetcode submit region end(Prohibit modification and deletion)
