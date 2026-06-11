# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempa=headA
        tempb=headB
        while tempa!=tempb:
            if tempa is None:
                tempa=headB
            else:
                tempa=tempa.next
            if tempb is None:
                tempb=headA
            else:
                tempb=tempb.next
        return tempa
        