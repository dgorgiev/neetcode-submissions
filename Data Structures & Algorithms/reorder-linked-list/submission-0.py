# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head.next
        dec = deque()
        while tail:
            dec.append(tail)
            tail = tail.next

        while dec:
            head.next = dec.pop()
            head = head.next
            if dec:
                head.next = dec.popleft()
                head = head.next
        head.next = None
            
        