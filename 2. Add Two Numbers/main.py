from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total_node = ListNode(0)  
        current = total_node      
        carry = 0                

        while l1 or l2 or carry:
            if l1: val1 = l1.val
            else: val1 = 0

            if l2: val2 = l2.val
            else: val2 = 0
            
            total = val1 + val2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)
            
            current.next = new_node
            current = new_node
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return total_node.next