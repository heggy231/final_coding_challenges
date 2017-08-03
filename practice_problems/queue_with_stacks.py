"""
Queue with stacks
"""

class Stack(object):
    """
    Stack class.
    """

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)



class Queue(object):
    """
    Implementing a queue using two stack objects.
    """

    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        if self.outbox.size() == 0:
            while self.inbox.size() != 0:
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()



test_queue = Queue()
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
print(test_queue.dequeue())


