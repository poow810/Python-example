# 헨젤과 그레텔의 집으로 돌아가기
import random

size = 10
stack = [None for _ in range(size)]
top = -1

def is_stack_full():
    global size, stack, top
    if top >= size-1:
        return True
    else:
        return False


def is_stack_empty():
    global size, stack, top
    if top == -1:
        return True
    else:
        return False


def push(data):
    global size, stack, top
    if is_stack_full():
        return
    top = top + 1
    stack[top] = data


def pop():
    global size, stack, top
    if is_stack_empty():
        return None
    data = stack[top]
    stack[top] = None
    top = top - 1
    return data


if __name__=="__main__":
    color = ["빨강", "주황", "노랑", "초록", "파랑", "보라"]
    random.shuffle(color)
    for i in color:
        push(i)
        print(i, '-->', end=" ")
    print("과자집")
    while True:
        i = pop()
        if i == None:
            break
        print(i, '-->', end=" ")
    print("우리집")