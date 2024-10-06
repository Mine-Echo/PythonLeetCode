# 合并K个升序数组


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        list1 = self.mergeKLists(lists[0 : len(lists) // 2])
        list2 = self.mergeKLists(lists[len(lists) // 2 :])
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        # merge list1 & list2
        return self.merge2Lists(list1, list2)

    def merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        node = head = ListNode(0, None)
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
        while list1:
            node.next = list1
            node = node.next
            list1 = list1.next
        while list2:
            node.next = list2
            node = node.next
            list2 = list2.next
        return head.next
