# 원형 연결 리스트
class Node():
    def __init__(self, data):
        self.data = data
        self.link = None


node1 = Node("다현")
node1.link = node1

node2 = Node("정연")
node1.link = node2
node2.link = node1

# 중간에 삽입
new_node = Node("재남")
new_node.link = node1.link
node1.link = new_node

# 중간 노드 삭제
node1.link = new_node.link
del(new_node)


current = node1
print(current.data, end=" ")
while current.link != node1:
    current = current.link
    print(current.data, end=" ")
