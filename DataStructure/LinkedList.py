class Node():
    def __init__(self, data):
        self.data = data
        self.link = None


pre, current, head = None, None, None
def print_node(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=" ")
    while current.link != start:
        current = current.link
        print(current.data, end=" ")
    print()


# 노드 삽입
def insert_node(find_data, idx_data):
    global head, current, pre

    # 첫 번째에 삽입
    if head.data == find_data:
        node = Node(idx_data)
        node.link = head
        last = head
        if last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    # 두 번째에 삽입
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(idx_data)
            node.data = idx_data
            node.link = current
            pre.link = node
            return

    # 마지막에 삽입
    node = Node(idx_data)
    node.data = idx_data
    current.link = node
    node.link = head


# 노드 삭제
def del_node(delete_data):
    global pre, current, head

    # 첫 번째 노드 삭제
    if head.data == delete_data:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    # 나머지 위치 노드 삭제
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del(current)
            return


# 노드 검색
def search_node(find_data):
    global pre, current, head

    current = head
    if current.data == find_data:
        return current
    while current.link != head:
        current = current.link
        if current.data == find_data:
            return current
