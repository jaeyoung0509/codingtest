from typing import List
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = rstList = ListNode(0) #val = 0 , next = None
        carry = 0 
        while l1 or l2 or carry :
            v1 = v2 = 0
            if l1 :
                v1 ,l1 = l1.val , l1.next
            if l2 :
                v2 , l2 = l2.val , l2.next
            carry  , val = divmod(v1 + v2 + carry , 10)
            rstList.next = ListNode(val)
            rstList = rstList.next
        return root.next