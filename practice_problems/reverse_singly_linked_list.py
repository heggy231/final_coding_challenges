"""
Reverse singly linked list
"""


class LinkedListNode(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return '<Node: {}>'.format(self.value)

class LinkedList(object):
    def __init__(self, head):
        self.head = head


    def reverse(self):
        if self.head is None:
            return
        current = self.head
        previous = None
        next = current.next

        while current is not None and next is not None:
            current.next = previous
            previous = current
            current = next
            next = next.next

        self.head = current
        self.head.next = previous

    def print_linked_list(self):
        current = self.head
        print_list = []

        while current is not None:
            print_list.append(current.value)
            current = current.next

        print("->".join([str(item) for item in print_list]))


six = LinkedListNode(6)
five = LinkedListNode(5, six)
four = LinkedListNode(4, five)
three = LinkedListNode(3, four)
two = LinkedListNode(2, three)
one = LinkedListNode(1, two)

test_linked_list = LinkedList(one)

test_linked_list.reverse()

test_linked_list.print_linked_list()
