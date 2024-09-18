class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # Calculate the size of the linked list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        loop = k % n
        loop = n - loop
        
        if n == 1 or loop == n:
            return head
        
        j = 0
        temp = head
        firstAddress = head
        
        while temp:
            j += 1
            if j == loop:
                firstAddress = temp.next
                temp.next = None
                break
            temp = temp.next
        
        temp = firstAddress
        while temp.next:
            temp = temp.next
        
        temp.next = head
        return firstAddress
