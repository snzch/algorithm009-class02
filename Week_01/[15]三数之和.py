# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_val = nums[l] + nums[r] + nums[i]
                if sum_val == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum_val < 0:
                    l += 1
                else:
                    r -= 1
        return res


if __name__ == "__main__":
    input_output = [
        [
            [], []
        ],
        [
            [0, 5, 3, 1, -5, -9],
            [[-5, 0, 5]]
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        r = solution.threeSum(i)
        if r != o:
            print('error')
# leetcode submit region end(Prohibit modification and deletion)
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if v > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_val = nums[l] + nums[r] + nums[i]
                if sum_val == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum_val < 0:
                    l += 1
                else:
                    r -= 1
        return res


if __name__ == "__main__":
    input_output = [
        [
            [], []
        ],
        [
            [0, 5, 3, 1, -5, -9],
            [[-5, 0, 5]]
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        r = solution.threeSum(i)
        if r != o:
            print('error')
# leetcode submit region end(Prohibit modification and deletion)
