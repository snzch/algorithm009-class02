# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。
#
#  示例:
#
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#  Related Topics 栈 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    # 双指针
    # 时间复杂度 O(n)
    # 空间复杂度 O(1)
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        l_max, r_max = height[0], height[-1]
        water = 0
        while l <= r:
            if l_max < r_max:
                water += max(0, l_max - height[l])
                l_max = max(l_max, height[l])
                l += 1
            else:
                water += max(0, r_max - height[r])
                r_max = max(r_max, height[r])
                r -= 1
        return water

    # 栈
    # 时间复杂度 O(n)
    # 空间复杂度 O(n)
    # def trap(self, height: List[int]) -> int:
    #     stack = []
    #     water = 0
    #     for i in range(len(height)):
    #         while stack and height[stack[-1]] < height[i]:
    #             min_height = height[stack.pop()]
    #             if not stack:
    #                 break
    #             max_height = min(height[stack[-1]], height[i])
    #             water += (max_height - min_height) * (i - stack[-1] - 1)
    #         stack.append(i)
    #     return water
# leetcode submit region end(Prohibit modification and deletion)
