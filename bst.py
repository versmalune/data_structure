import random
import pandas as pd

class BinarySearchTree:
    class Node:
        def __init__(self, key, value, left, right):
            self.key = key
            self.value = [value]
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None
        self.key_count = 0
        self.value_count = 0

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)
        self.value_count += 1

    def __insert(self, node, key, value):
        # when a new key inserted, key_count must be increased by 1 (except when the new key is already in the tree)
        if node is None:
            node = self.Node(key, value, None, None)
            self.key_count += 1
        else:
            if key < node.key:
                node.left = self.__insert(node.left, key, value)
            elif key == node.key:
                node.value.append(value)
            else:
                node.right = self.__insert(node.right, key, value)
        return node

    def in_order(self):
        for x in self.__in_order(self.root):
            yield x

    def __in_order(self, node):
        if not node:
            return
        if node.left:
            for n in self.__in_order(node.left):
                yield n
        yield node
        if node.right:
            for n in self.__in_order(node.right):
                yield n

    def find(self, key):
        return self.__find(self.root, key)

    def __find(self, node, key):
        # if the key exists, return the value of the corresponding node
        # else, return [] (empty list)
        if node is None:
            return [] #node is not None
        elif node.key == key:
            return node.value
        elif key < node.key:
            return self.__find(node.left, key)
        else:
            return self.__find(node.right, key)

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        # returns the height of the given node
        if not node:
            return 0
        l = self.__height(node.left)
        r = self.__height(node.right)
        return max(l, r) + 1
        

def print_stat(tree):
    print(f"Height = {tree.height()}")
    print("{:,} keys / {:,} values".format(tree.key_count, tree.value_count))


if __name__ == "__main__":
    #-------------------------------------------------
    # simple bst test
    tree = BinarySearchTree()
    print_stat(tree)
    tree.insert(5, "F")
    print_stat(tree)
    tree.insert(3, "E")
    tree.insert(8, "D")
    tree.insert(6, "C")
    print_stat(tree)
    tree.insert(7, "B")
    tree.insert(1, "A")
    for x in tree.in_order():
        print(f"{x.key}:{x.value}", end="->")
    print()
    print("Key=6", tree.find(6))
    print("Key=4", tree.find(4))
    print("Key=1", tree.find(1))
    print("Key=5", tree.find(5))
    print("Key=9", tree.find(9))
    print_stat(tree)

   # -------------------------------------------------
    # insert 100,000 datas to the tree
    t = BinarySearchTree()
    for i in range(100000):
        k = random.randint(0, 100000)
        t.insert(k, f"DATA {i}")
    print_stat(t)

    # #-------------------------------------------------
    # search for a word from Shakespeare plays, returns the line with the word
    bst = BinarySearchTree()
    df = pd.read_csv('Shakespeare_data.csv', dtype=str)
    print("Indexing all data ...")
    for index, row in df.iterrows():
        # slice by word and insert it to the key, and the whole row to the value
        keys = [x.upper() for x in row[5].split(" ")]
        value = " ".join([x for x in row if str(x) != 'nan'])
        for key in keys:
            # insert each (key, value) pair to the tree
            bst.insert(key, value)
    print("Done")
    print_stat(bst)
    while True:
        # get input keyword from the user and search for it from the tree
        keyword = input(">> Enter keyword ('\\q' for quit) : ")
        if keyword == '\\q':
            break
        result = bst.find(keyword.upper())
        print("\n".join(result))
        print("--- Found {} lines".format(len(result)))





# def __insert(self, node, key, value):
#     if not node: #node가 없으면, 즉 root값이 없으면
#         node = self.Node(key, value, None, None) #node를 새로 만들어 주고
#         self.key_count += 1 #key_count값 1 증가
#     else: #node가 있을 경우, 즉 root가 있을 경우
#         if key < node.key: #함수로 들어온 key값이 node의 key값보다 크다면
#             node.left = self.__insert(node.left, key, value)
#             #node의 왼쪽에 넣을 건데, 다시 __insert함수 호출해서 node있는지 확인해서 그 결과에 따라 추가
#         elif key == node.key: #함수로 들어온 key값이 node의 key과 같다면
#             node.value.append(value)
#             #node의 value값에 새로 들어온 value값을 append를 해 준다
#         else: #함수로 들어온 key값이 node의 key값보다 작다면
#             node.right = self.__insert(node.right, key, value)
#             # node의 오른쪽에 넣을 건데, 다시 __insert함수 호출해서 node있는지 확인해서 그 결과에 따라 추가
#     return node
