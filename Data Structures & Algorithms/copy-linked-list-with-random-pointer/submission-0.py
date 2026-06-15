"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        checker = {None: None}
        curr = head

        while curr:
            checker[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = checker[curr]

            clone.next = checker[curr.next]
            clone.random = checker[curr.random]
            curr = curr.next

        return checker[head]

        