# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list
        slow, fast = head, head
        comp = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while comp and prev:
            tmp1, tmp2 = comp.next, prev.next
            comp.next = prev
            prev.next = tmp1
            comp = tmp1
            prev = tmp2

            











