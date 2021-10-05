# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, n1: Optional[ListNode], n2: Optional[ListNode]) -> Optional[ListNode]:
        
        # method 1: iterative --------------------

        ll = curr = ListNode(0)

        # while there are still nodes in BOTH lists to compare against each other
        while n1 and n2:
            if n1.val < n2.val:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next

        # if there aren't anymore nodes in at least one list, add remaining nodes to the result
        curr.next = n1 or n2
        return ll.next


        # method 2: recursive --------------------

        if n1 and n2:
            
            # make sure each element of n1 is always smaller than the corresponding one of n2
            if n1.val > n2.val:
                n1, n2 = n2, n1
            n1.next = self.mergeTwoLists(n1.next, n2)
        return n1 or n2