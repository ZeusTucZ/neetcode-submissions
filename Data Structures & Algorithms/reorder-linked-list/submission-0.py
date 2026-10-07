# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = slow
        slow = slow.next
        prev.next = None
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        l1 = head
        l2 = prev

        while l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2
