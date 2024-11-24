# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1st approach two pass

        # count = 0 # to find length of the list
        # temp = head
        # while temp:
        #     count += 1
        #     temp = temp.next
        # if count == n: # head to be deleted
        #     return head.next
        
        # temp = head
        # traverse_from_front = count - n # l-n
        # while traverse_from_front != 1: # stop at node one before the node to be deleted
        #     temp = temp.next
        #     traverse_from_front -= 1
        
        # del_node = temp.next
        # temp.next = del_node.next
        # return head        

        # 2nd approach one pass
        temp = head
        for i in range(n): # move temp n steps
            temp = temp.next

        if temp == None:
            return head.next

        prev = head
        while temp.next:
            prev = prev.next
            temp = temp.next
        
        # prev will be the node one before the node to be deleted
        del_node = prev.next
        prev.next = del_node.next
        return head        