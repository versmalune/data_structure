class Stack: #first in last out
    def __init__(self): #constructor
        self.list = []

    def is_empty(self):
        return not self.list #list return -> boolean으로 return 값 받음

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]
    
s = Stack()
print(s.is_empty())
s.push(1)
s.push(2)
print(s.peek())
print(s.pop())
print(s.pop())