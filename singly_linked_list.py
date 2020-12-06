class SinglyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None #link 하나
    
    def __init__(self):
        self.head = None

    def insert_head(self, value): #head는 None -> node 생성하고 그의 next에도 node 연결
        #node 생성
        node = self.Node(value)
        #node의 next를 다음 node에 연결
        node.next = self.head
        #head가 node 가리킴
        self.head = node 

    def insert_tail(self, value):
        node = self.Node(value)
        if not self.head:
            self.head = node
            return
        p = self.head
        while p.next:
            p = p.next #O(n)
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
    p = p.next # 한 바퀴 돔
print()
    # 출력 결과 : 10 5