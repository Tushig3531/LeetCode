
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:
# Input: head = [], val = 1
# Output: []
# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_node=ListNode(next=head)
        previous=dummy_node
        current=head
        while current: #while current is not Null
            next_node=current.next
            if current.val==val:
                previous.next=next_node
            else:
                previous=current
            current=next_node
        return dummy_node.next
def create_linked_list(lst):
    if not lst:
        return None
    head=ListNode(lst[0])
    current=head
    for val in lst[1:]:
        current.next=ListNode(val)
        current=current.next
    return head

def print_ll(head):
    elements=[]
    current=head
    while current:
        elements.append(str(current.val))
        current=current.next
    print("-->".join(elements))
        
            
        

head = create_linked_list([1,2,6,3,4,5,6])
val = 6
new_head=removeElements(head,val)
print_ll(new_head)