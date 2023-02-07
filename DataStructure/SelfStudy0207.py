## 함수 선언부
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def search(group):
    global current, root, left, right
    current = root
    while True:
        if group == current.data:
            print(f"{group}을(를) 찾음")
            break
        elif group < current.data:
            if current.left == None:
                print(f"{group}이(가) Tree에 없음")
                break
            current = current.left
        else:
            if current.right == None:
                print(f"{group}이(가) Tree에 없음")
                break
            current = current.right

root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스', '잇지', '여자친구']
node = TreeNode()
node.data = nameAry[0]
root = node

for name in nameAry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right


if __name__=="__main__":
    group = input("찾을 그룹이름 --> ")
    search(group)