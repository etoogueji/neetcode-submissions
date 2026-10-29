# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Hash map to map old node -> new copy node
        # Include None mapping to handle null pointers gracefully
        old_to_copy = {None: None}

        # First pass: Create all new nodes without assigning pointers
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: Connect next and random pointers
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]