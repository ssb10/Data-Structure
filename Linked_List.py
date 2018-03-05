class Node(object):
    def __init__(self, value, tail = None):
        self.value = value
        self.next = tail

class LinkedList(object):
    def __init__(self, *args):
        self.head = None

        for a in args:
            self.prepend(a)

    def prepend(self, value):
        """Insert value in forn of the list"""
        self.head = Node(value, self.head)

    def remove(self, value):
        """Remove specified value from the list"""
        n = self.head
        prev = None

        while n != None:
            if n.value == value:
                if prev == None:
                    self.head = self.head.next
                else:
                    prev.next = n.next
                return True
            prev = n
            n = n.next
        return False

    def pop(self):
        """Remove the first value from the list"""
        if self.head is None:
            print("Empty List!")
        value = self.head.value
        self.head = self.head.next
        return value

    def __iter__(self):
        n = self.head
        while n != None:
            yield n.value
            n = n.next

    def __repr__(self):
        if self.head is None:
            return 'Linked_List:[]'

        return 'Linked_List:[' + ' , '.join(map(str,self))+']'





