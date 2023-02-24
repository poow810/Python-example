# 스택에 데이터 삽입
def push(data):
    global Size, top, stack
    top += 1
    stack[top] = data


# 스택에서 데이터 추출
def pop():
    global Size, top, stack
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def is_empty_stack():
    global stack, Size, top
    if (top == -1):
        return True
    else:
        return False

# 응용
def check_bracket(word):
    for i in word:
        if i in '([{<':
            push(i)
        elif i in ')]}>':
            out = pop()
            if i == ')' and out == '(':
                pass
            elif i == ']' and out == '[':
                pass
            elif i == '}' and out == '{':
                pass
            elif i == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if is_empty_stack():
        return True
    else:
        return False

Size = 100
stack = [None for _ in range(Size)]
top = -1

if __name__=="__main__":

    words = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']
    for i in words:
        top = -1
        print(i, ' : ', check_bracket(i))