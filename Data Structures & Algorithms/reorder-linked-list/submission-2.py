# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the midsection
        starter = ListNode(0, head)
        slow = fast = starter
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #assign slow to next to start of second part
        secondP = slow.next
        slow.next = None
        firstP = head
        #reverse second part
        prev, curr = None, secondP
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        secondP = prev

        firstP = head
        while secondP:  
        # Save the natural next steps
           tmp1 = firstP.next
           tmp2 = secondP.next

           firstP.next = secondP
           secondP.next = tmp1

           firstP = tmp1
           secondP = tmp2