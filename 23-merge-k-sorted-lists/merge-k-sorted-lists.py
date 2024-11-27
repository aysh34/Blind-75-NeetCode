# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        head = lists[0] # 1st list
        for i in range(1,len(lists)):
            head = self.merge2Lists(head,lists[i])
        return head

            

    def merge2Lists(self,l1,l2):
        # dummy = ListNode()
        # temp = dummy # for traversal
        # while l1 and l2:
        #     if l1.val<l2.val:
        #         temp.next = l1
        #         l1 = l1.next
        #     else:
        #         temp.next = l2
        #         l2 = l2.next
        #     temp = temp.next
        
        # temp.next = l1 or l2 # in case of unequal lenghth, which ever is remaining
        # return dummy.next
        
        if not l1: # recursive approach
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next = self.merge2Lists(l1.next,l2)
            return l1
        elif l2.val<=l1.val:
            l2.next = self.merge2Lists(l2.next,l1)
            return l2
        