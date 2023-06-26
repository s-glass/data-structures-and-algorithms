from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            raise Exception("The queue is empty.")

        return self.stack1.pop()





