# 노드 생성
class Node():
    def __int__(self):
        self.data = None
        self.link = None


# 연결 리스트 생성
def print_node(start):
    current = start
    if current == None:
        return
    while current.link != None:
        current = current.link


# data 삽입
def insert_data(find_data, idx_data):
    global memory, head, current, pre

    # 첫 번째 노드 삽입
    if head.data == find_data:
        node = Node()
        node.data = idx_data
        node.link = head
        head = node
        return

    # 중간에 삽입
    current = head
    while current.data != None:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = idx_data
            node.link = current
            pre.link = node
            return

    # 마지막에 삽입
    node = Node()
    node.data = insert_data()
    current.link = node


# data 삭제
def del_data(idx_data):
    global current, pre, head, memory

    # 첫 번째 삭제
    if head.data == idx_data:
        current = head
        head = head.link
        del(current)
        return


    # 나머지 삭제
    current = head
    while current.data != None:
        pre = current
        current = current.link
        if current.data == idx_data:
            current.link = pre.link
            del(current)
            return



# data 검색
def search_data(idx_data):
    global memory, current, pre, head

    current = head
    if current.data == idx_data:
        return current
    while current.link != None:
        current = current.link
        if current.data == idx_data:
            return current
    return Node()


