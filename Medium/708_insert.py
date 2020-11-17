"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        p1 = head
        temp = Node(insertVal)
        if head==None:
            temp.next = temp
            return temp
        
        max_val = -float('inf')
        min_val = float('inf')
        
        while p1.next!=head:
            max_val = max(max_val, p1.val)
            min_val = min(min_val, p1.val)
            p1 = p1.next
            
        max_val = max(max_val, p1.val)
        min_val = min(min_val, p1.val)
    
        # print(max_val, min_val)
    
        prev = head
        p1 = head.next

        
        while True:
            if p1.val > insertVal and prev.val <= insertVal:
                temp.next = p1
                prev.next = temp
                return head

            if p1.val==min_val and min_val >= insertVal and p1.val!=prev.val: 
                temp.next = p1
                prev.next = temp
                return head
            
            if p1.val==min_val and insertVal >= max_val and p1.val!=prev.val:
                temp.next = p1
                prev.next = temp
                return head
            
            prev = p1
            p1 = p1.next
        
            if prev==head:
                break
                
        temp.next = prev.next
        prev.next = temp
        return head
        
