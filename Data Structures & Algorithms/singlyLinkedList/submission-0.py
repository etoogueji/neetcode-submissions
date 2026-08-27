class Node:
    def __init__(self, val: int=0, next: 'Node'=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        # a dummy node to avoid any 'if self.head is None' case
        # the actual first node is self.head.next
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, i: int) -> int:
        curr = self.head.next
        index = 0
        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            index += 1
        return -1


    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head.next)
        self.head.next = new_node 
        if self.tail == self.head: #if list is currently empty
            self.tail = new_node

        

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, i: int) -> bool:
        index = 0
        curr = self.head

        while index < i and curr:
            curr = curr.next
            index += 1

        if not curr or not curr.next:
            return False

        if curr.next == self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        return True
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
