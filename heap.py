class MaxHeap:
    def __init__(self):
        self.list = []
    
    def __parent(self, i):
        return int((i + 1) / 2 ) - 1

    def __left(self, i):
        return 2 * i + 1

    def __right(self, i):
        return 2 * i + 2


    def push(self, value):
        # Big O : log(n)
        self.list.append(value)
        curr = len(self.list) - 1
        p = self.__parent(curr)
        while curr > 0 and self.list[curr] > self.list[p]:
            self.list[curr], self.list[p] = self.list[p], self.list[curr]
            curr = p
            p = self.__parent(curr)
        return

    def __bigger_child(self, i):
        left = self.__left(i)
        right = self.__right(i)

        if len(self.list) <= left:
            return None
        if len(self.list) <= right or self.list[left] > self.list[right]:
            return left
        else:
            return right


    def pop(self):
        if (len(self.list)) == 0:
            return None
        elif len(self.list) == 1:
            return self.list.pop()

        ret = self.list[0]
        self.list[0] = self.list.pop()
        p = 0 #parent
        c = self.__bigger_child(p) #current

        while c and self.list[p] < self.list[c]:
            self.list[p], self.list[c] = self.list[c], self.list[p]
            p = c
            c = self.__bigger_child(p)
        return ret


    def peek(self):
        if (len(self.list)) == 0:
            return None
        return self.list[0]

    def print(self):
        print (self.list)


heap = MaxHeap()
data = [10, 9, 28, 30, 5, 7, 12, 8]
for i in data:
    heap.push(i)
    print(heap.list)

print(heap.pop())
