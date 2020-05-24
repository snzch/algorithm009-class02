# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        fake = pre = ListNode(None)
        fake.next = head
        while head and head.next:
            nex = head.next
            head.next = nex.next
            nex.next = head
            pre.next = nex
            pre = head
            head = head.next
            # head.next.next, head.next, pre.next, pre, head = head, head.next.next, head.next, head, head.next.next

        return fake.next
# leetcode submit region end(Prohibit modification and deletion)
