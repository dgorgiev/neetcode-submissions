# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        i = 0
        while node:
            i += 1
            node = node.next
        
        target = i - n + 1
        i = 1
        node = head
        prev = None
        nex = node.next
        if target == 1:
            tmp = head.next
            head.next = None
            return tmp
        while True:
            if i == target:
                prev.next = nex
                break
            prev = node
            node, nex= nex, nex.next
            i += 1

        return head