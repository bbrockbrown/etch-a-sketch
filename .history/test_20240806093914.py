class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next

    dummy = ListNode()
    while stack:
        node = stack.pop()
        node_val = node.val
        dummy.next = ListNode(node_val)
        dummy = dummy.next
    return dummy.next

new = reverseList(ListNode(0, ListNode(1, ListNode(2, ListNode(3, None)))))
while new:
    print(new.val)
    new = new.next