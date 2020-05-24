from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = pre = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return fake.next


def list2node(nums: List[int]):
    fake = pre = ListNode(None)
    for n in nums:
        node = ListNode(n)
        pre.next = node
        pre = node
    return fake.next


def node2list(head: ListNode):
    r = []
    while head:
        r.append(head.val)
        head = head.next
    return r


if __name__ == "__main__":
    input_output = [
        [
            [[1, 2, 3, 4, 5], [3, 5, 7, 9]],
            [1, 2, 3, 3, 4, 5, 5, 7, 9]
        ]
    ]
    solution = Solution()
    for i, o in input_output:
        l1 = list2node(i[0])
        l2 = list2node(i[1])
        res = node2list(solution.mergeTwoLists(l1, l2))
        if res != o:
            print('error')