class CircularQueue:  
    def __init__(self, max_size):
        self.max_size = max_size + 1
        self.queue = [None] * self.max_size # define queue size
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        # adds data to the queue
        # if full, do not add data and return None
        # if enqueued successfully, return True
        if self.is_full():
            return None
        else:
            self.queue[self.rear % self.max_size] = data
            self.rear += 1
            return True

    def dequeue(self):
        # if the queue is empty, return None
        # else, return the data in the queue
        if self.is_empty():
            return None
        else:
            pop_item = self.queue[self.front % self.max_size]
            self.queue[self.front % self.max_size] = None
            self.front += 1
            return pop_item

    def is_full(self):
        # if the queue is full, return True
        # else, return False
        if (self.rear + 1) % self.max_size == self.front:
            return True
        else:
            return False

    def is_empty(self):
        # if the queue is empty, return True
        # else, return False
        if self.rear == self.front:
            return True
        else:
            return False

    def size(self):
        # returns the current number of items in the queue
        size = self.rear - self.front
        return size


if __name__ == "__main__":
    q = CircularQueue(3)
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Enque 10", q.enqueue(10))
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())
    print("Enque 20", q.enqueue(20), q.size())
    print("Enque 30", q.enqueue(30), q.size())
    print("Enque 40", q.enqueue(40), q.size())
    print("Deque", q.dequeue(), q.size())
    print("Enque 50", q.enqueue(50), q.size())
    print("Deque", q.dequeue(), q.size())
    print("Deque", q.dequeue(), q.size())
    print("Enque 60", q.enqueue(60), q.size())
    print("Enque 70", q.enqueue(70), q.size())

    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print("Deque", q.dequeue(), q.size())
    print("Empty?", q.is_empty(), ", Full?", q.is_full(), ", Size=", q.size())

    print(len(q.queue)) # should be 4. list 자체의 크기는 변하지 않아야 함!!!


"""
Empty? True , Full? False , Size= 0
Enque 10 True
Empty? False , Full? False , Size= 1
Enque 20 True
Enque 30 True
Enque 40 None
Deque 10
Enque 50 True
Deque 20
Deque 30
Enque 60 True
Enque 70 True
Empty? False , Full? True , Size= 3
Deque 50
Empty? False , Full? False , Size= 2
Deque 60
Empty? False , Full? False , Size= 1
Deque 70
Empty? True , Full? False , Size= 0
Deque None
Empty? True , Full? False , Size= 0
4
"""
