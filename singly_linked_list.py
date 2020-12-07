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
    
    
    
    def traverse(self): # generator
        p = self.head
        while p:
            yield p.value # when yield, stop running and return iterator
            p = p.next

    def find(self, value):
        p = self.head
        while p:
            if value == p.value:
                return True
            p = p.next
        return False
        
        # when using generator
        # for val in self.traverse():
            # if value == val:
                # return True
            # return False

    def get_at(self, idx):
        cnt = 0
        p = self.head
        while p:
            if cnt == idx:
                return p.value
            cnt += 1
            p = p.next
        return None
    
     def print(self):
        p = self.head # points the current node
        while p: # while there is a value in the node
            print(p.value, end='->')
            p = p.next # print the value of the node, and change p to the next node
        print()

        # when using generator
        # for val in self.traverse():
            # print(val, end = '->')
        # print()


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
