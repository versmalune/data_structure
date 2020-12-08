"""
학번: 60171670
이름: 홍유진
"""
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
        # 여기에 Tree의 노드에 key, value를 insert하는 알고리즘을 작성하시오.
        # 새로운 키가 추가되면 key_count도 증가시켜야 함 (동일한 키가 들어오는 경우는 증가 안함)
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
        # 키가 존재하지 않으면 [] (빈 리스트)를 반환하시오.
        # 키가 존재하면 node.value를 반환하시오.'
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
        # 주어진 노드의 높이를 반환하는 알고리즘을 작성하시오.
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
    # 간단한 BST 테스트
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
    # 10만개 데이터 넣는 실험
    t = BinarySearchTree()
    for i in range(100000):
        k = random.randint(0, 100000)
        t.insert(k, f"DATA {i}")
    print_stat(t)

    # #-------------------------------------------------
    # 세익스피어의 희곡에서 단어를 검색하는 실험
    # 단어를 입력하면 해당 단어가 나오는 희곡의 라인을 검색해줌.
    bst = BinarySearchTree()

    # csv 파일을 읽어들인다.
    df = pd.read_csv('Shakespeare_data.csv', dtype=str)
    print("Indexing all data ...")
    for index, row in df.iterrows():
        # 대사를 단어단위로 잘라 keys 리스트에 저장하고, 전체 행은 합쳐 value에 저장한다.
        keys = [x.upper() for x in row[5].split(" ")]
        value = " ".join([x for x in row if str(x) != 'nan'])
        for key in keys:
            # 각 key, value를 트리에 저장한다.
            bst.insert(key, value)
    print("Done")
    print_stat(bst)
    while True:
        # 사용자에게 keyword를 입력받아서 트리에서 찾아준다.
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
