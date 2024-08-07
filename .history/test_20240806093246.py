class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    stack = []
    curr = head
    while curr.next:
        stack.append(curr)
        curr = curr.next

    dummy = ListNode()
    while stack:
        new_node = stack.pop()
        dummy.next = new_node
        dummy = dummy.next
    return dummy.next

reverseList()