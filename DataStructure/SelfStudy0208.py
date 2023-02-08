class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = None
stack = []
visitedAry = []  # 방문한 정점
name = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']

G1 = Graph(6)
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5
G1.graph[0][1] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][3] = 1
G1.graph[3][1] = 1; G1.graph[3][2] = 1; G1.graph[3][4] = 1; G1.graph[3][5] = 1
G1.graph[4][3] = 1; G1.graph[4][5] = 1;
G1.graph[5][3] = 1; G1.graph[5][4] = 1;

print('## G1 무방향 그래프 ##')
for row in range(6):
    for col in range(6):
        print(G1.graph[row][col], end=' ')
    print()

current = 0  # 시작 정점 A
stack.append(current)
visitedAry.append(current)

while (len(stack) != 0):
    next = None
    for vertex in range(6):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                pass
            else:  # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break

    if next != None:  # 다음에 방문할 정점이 있는 경우
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:  # 다음에 방문할 정점이 없는 경우
        current = stack.pop()

print('방문 순서 -->', end='')
for i in visitedAry:
    print(name[i], end='   ')
