# # 노드 생성
# class Node():
#     def __int__(self):
#         self.data = None
#         self.link = None
#
#
# # 연결 리스트 생성
# def print_node(start):
#     current = start
#     if current == None:
#         return
#     while current.link != None:
#         current = current.link
#
#
# # data 삽입
# def insert_data(find_data, idx_data):
#     global memory, head, current, pre
#
#     # 첫 번째 노드 삽입
#     if head.data == find_data:
#         node = Node()
#         node.data = idx_data
#         node.link = head
#         head = node
#         return
#
#     # 중간에 삽입
#     current = head
#     while current.data != None:
#         pre = current
#         current = current.link
#         if current.data == find_data:
#             node = Node()
#             node.data = idx_data
#             node.link = current
#             pre.link = node
#             return
#
#     # 마지막에 삽입
#     node = Node()
#     node.data = insert_data()
#     current.link = node
#
#
# # data 삭제
# def del_data(idx_data):
#     global current, pre, head, memory
#
#     # 첫 번째 삭제
#     if head.data == idx_data:
#         current = head
#         head = head.link
#         del(current)
#         return
#
#
#     # 나머지 삭제
#     current = head
#     while current.data != None:
#         pre = current
#         current = current.link
#         if current.data == idx_data:
#             current.link = pre.link
#             del(current)
#             return
#
#
#
# # data 검색
# def search_data(idx_data):
#     global memory, current, pre, head
#
#     current = head
#     if current.data == idx_data:
#         return current
#     while current.link != None:
#         current = current.link
#         if current.data == idx_data:
#             return current
#     return Node()
import random


# 로또 추첨하기
class Node():
    def __init__(self, data):
        self.data = data
        self.link = None


def print_node(start):
    current = start
    if current == None:
        return
    print(current.data)
    while current.link != None:
        current = current.link
        print(current.data)


# 번호 정렬하여 연결 리스트 만드는 함수
def make_lotto(num):
    global current, pre, head, memory
    print_node(head)

    # 첫 번째 삽입
    node = Node(num)
    node.data = num
    if head == None:
        head = node
        return
    if head.data > num:
        head.link = head
        head = node
        return

    # 중간에 삽입
    current = head
    if current.data != None:
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current
            return
    current.link = node


# 중복되는 번호가 있는지 찾는 함수
def find_num(num):
    global memory, pre, current, head

    head = Node(num)
    if head == None:
        return False
    current = head
    if current.data == num:
        return True
    while current.link != None:
        current.link = current
        if current.data == num:
            return True
    return False


head, current, pre = None, None, None
num_list = [random.randint(1,45) for i in range(6)]
lotto_count = 0

for i in range(len(num_list)):
    if find_num(num_list[i]):
        continue
    lotto_count += 1
    make_lotto(num_list[i])
    if lotto_count >= 6:
        break

print_node(head)