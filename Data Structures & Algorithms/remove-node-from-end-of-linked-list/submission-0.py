# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        count = 0

        while tail:
            tail = tail.next
            count += 1

        count -= n

        if count == 0:
            return head.next

        curr = head
        prev = None
        while count > 0:
            prev = curr
            curr = curr.next
            count -= 1

        prev.next = curr.next
        return head
        