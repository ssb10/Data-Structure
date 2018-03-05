class Node(object):
    def __init__(self, value, tail = None):
        self.value = value
        self.next = tail

class Queue_using_LinkedList(object):
    """Pointer Based Queue using Linked List"""
    def __init__(self, *args):
        self.head = None
        self.tail = None

        #for a in args:
          #  self.append(a)

    def append(self, value):
        """Insert new value at the end of the queue"""
        n = Node(value)

        if self.head is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def is_empty(self):
        """Check if the queue is empty"""
        return self.head == None

    def pop(self):
        """Remove the oldest value i.e. the first value from the queue"""
        if self.head is None:
            print("Queue is empty!")
        else:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head is None:
            return 'queue:[]'
        else:
            return 'queue:['+' , '.join(map(str,self))+"]"