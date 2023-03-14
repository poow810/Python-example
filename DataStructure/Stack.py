import sys

def push(data):
    global top, size, stack

    top = top + 1
    stack[top] = data


def is_stack_empty():
    global Size
    if top == Size-1:
        return 1
    else:
        return 0


def pop():
    global top, stack, size
    if is_stack_empty():
        return -1
    data = stack[top]
    stack[top] = None
    top = top - 1
    return data


def size():
    global stack
    return len(stack)


def top():
    if is_stack_empty():
        return -1
    return stack[-1]


N = int(input())
top = -1
stack = []
num = 0
Size = 100000
for i in range(N):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'top':
        if is_stack_empty():
            print(-1)
        print(stack[-1])

    elif a[0] == 'size':
        print(size())

    elif a[0] == 'empty':
        print(is_stack_empty())

    elif a[0] == 'pop':
        print(pop())
    else:
        push(a[1])