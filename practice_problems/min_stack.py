
import math
class minStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, item):
        if len(self.mins) == 0:
            self.mins.append(item)
        else:
            if item < self.mins[-1]:
                self.mins.pop()
                self.mins.append(item)
        self.stack.append(item)

    def pop(self):
        item_to_remove = self.stack.pop()
        if len(self.mins) > 0:
            if self.mins[-1] == item_to_remove:
                self.mins.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack[0]

    def min(self):
        if len(self.mins) > 0:
            return self.mins[-1]

test_stack = minStack()
test_stack.push(-3)
test_stack.push(1)
test_stack.push(5)
test_stack.push(-9)
print(test_stack.stack)
print(test_stack.mins)
print(test_stack.min())


