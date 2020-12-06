"""
학번: 60171670
이름: 홍유진
"""
class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
        def __str__(self):
            return f"NODE[{self.value}]"

    def __init__(self):
        self.head = self.Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def is_empty(self):
        return (self.size == 0)

    def add_after(self, node, value):
        new_node = self.Node(value)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.size +=1

    def add_before(self, node, value):
        new_node = self.Node(value)
        new_node.prev = node.prev
        new_node.next = node
        node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def add_head(self, value):
        self.add_after(self.head, value)

    def add_tail(self, value):
        self.add_before(self.head, value)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_head(self):
        if not self.is_empty():
            self.remove(self.head.next)

    def remove_tail(self):
        if not self.is_empty():
            self.remove(self.head.prev)

    def traverse(self, dir = 1):
        # generator를 이용하여 리스트를 정방향(dir=1) 혹은 역방향(dir=-1)으로 순회할 수 있도록 함
        node = self.head.next if dir == 1 else self.head.prev
        while node != self.head:
            yield node
            node = node.next if dir == 1 else node.prev

    def find(self, value, from_node = None):
        if from_node == None:
            from_node = self.head
        node = from_node.next
        while node != self.head:
            if node.value == value:
                return node
            node = node.next
        return None

    def print(self, dir = 1):
        print("FORWARD: " if dir==1 else "BACKWARD:", end = "")
        for node in self.traverse(dir):
            print(node.value, end="->")
        print()




if __name__ == "__main__":
    list = LinkedList()
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())
    list.add_head(1)
    list.add_head(3)
    list.add_tail(3)
    list.add_tail(4)
    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    a = list.find(3)
    print(a)
    b = list.find(3, from_node=a)
    print(b)
    list.add_before(b, 9)
    list.add_after(b, 5)

    list.print()
    list.print(-1)

    c = list.find(4)
    list.remove(c)

    list.print()
    list.print(-1)

    list.remove_head()
    list.remove_head()

    list.print()
    list.print(-1)

    list.remove_tail()
    list.remove_tail()

    list.print()
    list.print(-1)
    print("IS_EMPTY?", list.is_empty())

    list.remove_head()
    list.print()
    print("IS_EMPTY?", list.is_empty())


"""
FORWARD:
BACKWARD:
IS_EMPTY? True
FORWARD: 3->1->3->4->
BACKWARD: 4->3->1->3->
IS_EMPTY? False
NODE[3]
NODE[3]
FORWARD: 3->1->9->3->5->4->
BACKWARD: 4->5->3->9->1->3->
FORWARD: 3->1->9->3->5->
BACKWARD: 5->3->9->1->3->
FORWARD: 9->3->5->
BACKWARD: 5->3->9->
FORWARD: 9->
BACKWARD: 9->
IS_EMPTY? False
FORWARD:
IS_EMPTY? True
"""