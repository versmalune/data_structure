import random

class BST:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        
    def __addNode(self, node, key):
        if node:
            if node.key > key:
                node.left = self.__addNode(node.left, key)
            elif node.key < key:
                node.right = self.__addNode(node.right, key)
        else:
            node = self.Node(key)
        return node

    def add(self, key):
        self.root = self.__addNode(self.root, key)

    def __inorder(self, node):
        if node:
            self.__inorder(node.left)
            print(node.key, end=" ")
            self.__inorder(node.right)

    def inorder(self):
        self.__inorder(self.root)
        print()

    def __height(self, node):
        if not node:
            return 0
        l = self.__height(node.left)
        r = self.__height(node.right)
        return max(l, r) + 1

    def height(self):
        return self.__height(self.root)
        
    # def search(self, key):


t = BST()
for _ in range(100):
    t.add(random.randint(0, 1000))
t.inorder()
print(t.height()) # 10 # the height doesn't increase exponentially
# t.search(10)
