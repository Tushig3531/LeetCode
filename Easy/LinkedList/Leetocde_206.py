# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def reverseList(head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        daraagin_node=ListNode(head=next)
        previous=None
        current=head
        while current:
            current.next=previous
            previous=current
            current.next_node
            