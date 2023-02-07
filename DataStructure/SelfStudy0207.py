# 7-1
def enQueue(data):
    global Size, queue, front, rear
    if rear == Size-1:
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data


Size = 5
queue = ["화사", "솔라", "문별", "휘인", None]
front = -1
rear = 3

print(queue)
enQueue("선미")
print(queue)
enQueue("재남")
