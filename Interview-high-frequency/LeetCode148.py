# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
冒泡排序：超时
"""
# class Solution(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """

#         # 计算链表长度
#         node = head
#         cnt = 0
#         while node != None:
#             cnt += 1
#             node = node.next
#         head = ListNode(0, head)
#         # 冒泡排序
#         for i in range(cnt - 1):
#             pre = head
#             now = head.next
#             next = now.next
#             for j in range(cnt - 1 - i):
#                 if now.val > next.val:
#                     self.swap(pre, now, next)
#                 pre = pre.next
#                 now = pre.next
#                 next = now.next
#         return head.next

#     def swap(self, pre, node1, node2):
#         pre.next = node2
#         node1.next = node2.next
#         node2.next = node1

'''
归并排序
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.sort(head, None)

    def sort(self, head: ListNode, tail: ListNode) -> ListNode:
        if head == tail:
            return None
        if head.next == tail:
            head.next = None
            return head
        fast = head
        slow = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        return self.merge(self.sort(head, slow), self.sort(slow, tail))

    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        node = dummyHead = ListNode()
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
        while head1 != None:
            node.next = head1
            node = node.next
            head1 = head1.next
        while head2 != None:
            node.next = head2
            node = node.next
            head2 = head2.next
        return dummyHead.next


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
    result = Solution().sortList(head)
