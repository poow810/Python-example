import random


# 응용예제 2번 - 로또 추첨하기
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_node(first):
    current = first
    if current == None:
        return
    print(current.data, end=" ")
    while current.link != None:
        current = current.link
        print(current.data, end=" ")



def insert_number(number):
    global list, head, current, pre
    # 첫 번째에 삽입
    node = Node()
    node.data = number
    if head == None:
        head = node
        return
    if head.data > number:
        node.link = head
        head = node
        return
    # 중간 이후 삽입
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data > number:
            pre.link = node
            node.link = current
            return

    current.link = node

def find_number(number):
    global head, current, pre
    if head == None:
        return False
    current = head
    if current.data == number:
        return True
    while current.link != None:
        current = current.link
        if current.data == number:
            return True
    return False


pre, current, head = None, None, None


if __name__=="__main__":
    count = 0
    while True:
        num = random.randint(1, 45)
        if find_number(num):
            continue
        count = count + 1
        insert_number(num)
        if count == 6:
            break

    print_node(head)
