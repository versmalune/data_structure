class SinglyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None # a single link
    
    def __init__(self):
        self.head = None

    def insert_head(self, value): # init head = None, create node and connect it to a new node by next
        # create node
        node = self.Node(value)
        # connect newly created node's next to the previous head node
        node.next = self.head
        # head pointing the newly created node
        self.head = node 

    def insert_tail(self, value):
        node = self.Node(value)
        if not self.head:
            self.head = node
            return
        p = self.head
        while p.next:
            p = p.next # O(n)
        p.next = node


    def delete_head(self):
        if not self.head:
            return None
        node = self.head
        self.head = node.next
        return node.value


list = SinglyLinkedList()
list.insert_head(5)
list.insert_head(10)
list.insert_head(3)
v = list.delete_head()
print(v) #3

list.insert_tail(7)
list.insert_tail(2)


p = list.head
while p:
    print(p.value, end = " ")
    p = p.next # makes one round
print()
    # result: 10 5
