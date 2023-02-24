# 이중 연결 리스트 구현
class Node():
    def __init__(self, data):
        self.data = data
        self.nlink = None
        self.plink = None


def print_node(start):
    current = start
    if current.nlink == None:
        return
    print(current.data, end=" ")
    while current.nlink != None:
        current = current.nlink
        print(current.data)
    print(current.data, end=" ")
    while current.plink != None:
        current = current.plink
        print(current.data)


pre, current, head = None, None, None
data_list = ["다현", "정연", "쯔위", "사나", "지효"]

if __name__=="__main__":

    node = Node(data_list[0])
    head = node

    for data in data_list[1:0]:
        pre = node
        node = Node(data_list[1:])
        pre.nlink = node
        node.plink = pre

    print_node(head)