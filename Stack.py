class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        """to insert value into the stack"""
        self.stack.append(value)

    def pop(self):
        """to pop value from the stack if it is not empty"""
        if len(self.stack) == 0:
            print("The Stack is Empty!")
        else:
            return self.stack.pop()

    def is_empty(self):
        """check if the stack is empty"""
        return len(self.stack) == 0

    def display(self):
        return str(self.stack)

print("--Stack Implementation--")

s = Stack()
s.push(8)
d=s.display()
print(d)
s.push(9)
d=s.display()
print(d)
s.pop()
s.is_empty()
d=s.display()
print(d)

