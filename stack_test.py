import unittest
from stack import Stack
class TestStack(unittest.TestCase): #unittest상속
    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty) #참이 아니면 무조건 fail
        s.push(1)
        self.assertTrue(s.is_empty)
        s.pop()
        self.assertTrue(s.is_empty)

    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push("A")
        self.assertEqual(s.pop(), "A")
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

if __name__ == '__main__':
    unittest.main()