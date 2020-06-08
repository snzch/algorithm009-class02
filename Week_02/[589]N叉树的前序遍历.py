# 给定一个 N 叉树，返回其节点值的后序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其后序遍历: [5,6,3,2,4,1].
#
#
#
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        # res = []
        #
        # def helper(node: 'Node'):
        #     if node:
        #         for n in node.children:
        #             helper(n)
        #         res.append(node.val)
        # helper(root)
        # return res
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res

# leetcode submit region end(Prohibit modification and deletion)
