
class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next  = None



a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

def kth_last_node(k, head):
    """
    >>> kth_last_node(2, a)
    "Devil's Food"
    >>> kth_last_node(3, a)
    'Cheese'
    >>> kth_last_node(5, a)
    'Angel Food'
    """
    if head is None:
        return
    else:
        current = head
        size = 1
        while current.next is not None:
            current = current.next
            size += 1

        current = head
        counter = 1
        while current.next is not None:
            if counter == (size - k + 1):
                return current.value
            current = current.next
            counter += 1


