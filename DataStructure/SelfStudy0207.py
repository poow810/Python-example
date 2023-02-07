# 7-2
def is_queue_full():
    global Size, queue, front, rear
    if rear == Size -1:
        return True
    else:
        return False


def de_queue():
    global Size, queue, front, rear
    if front == rear:
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data


Size = 5
front = -1
rear = 0
queue = ["화사", None, None, None, None]

print(queue)
print(f"추출한 데이터 --> {de_queue()}")
print(queue)
print("큐가 비었습니다.")