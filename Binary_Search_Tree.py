class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_to_subtree(self, p, value):
        if p is None:
            return Node(value)

        p.add(value)
        return p

    def add(self, value):
        if value <= self.value:
            self.left = self.add_to_subtree(self.left, value)
        elif value > self.value:
            self.right = self.add_to_subtree(self.right, value)

    def remove_from_subtree(self, p, value):
        if p:
            return p.remove(value)
        return None

    def remove(self, value):
        if self.value <= value:
            self.left = self.remove_from_subtree(self.left, value)
        elif self.value > value:
            self.right = self.remove_from_subtree(self.right, value)
        else:
            #find largest value in left subtree
            if self.left is None:
                return self.right

        child = self.left
        while child.right:
            child = child.right

        self.left = self.remove_from_subtree(self.left, child.value)
        self.value = child.value

        return self

    def inorder_traversal(self):
        if self.left:
            for n in self.left.inorder_traversal():
                yield n

        yield self.value

        if self.right:
            for n in self.right.inorder_traversal():
                yield n



class BinarySearchTree():
    def __init__(self):
        self.root = None

    def addNode(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def __contains__(self, value):
        r = self.root
        while r is not None:
            if value < r.value:
                r = r.left
            elif value > r.value:
                r = r.right
            else:
                return True

        return False

    def removeNode(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)

    def findClosest(self, value):
        if self.root is None:
            return None

        n = self.root
        best_match = n
        difference = abs(self.root.value - value)
        while n:
            if abs(n.value - value) < difference:
                best_match = n
                difference = n.value - value
            if value < n.value:
                n = n.left
            elif value > n.value:
                n = n.right
            else:
                return value

        return best_match.value

    def getmin(self):
        if self.root is None:
            print("BST is empty!")
        n = self.root
        while n.left:
            n = n.left
        return n.value

    def getmax(self):
        if self.root is None:
            print("BST is empty!")
        n = self.root
        while n.right:
            n = n.right
        return n.value

    def __iter__(self):
        if self.root:
            for n in self.root.inorder_traversal():
                yield n
