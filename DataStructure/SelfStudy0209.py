# 10-1 두 수를 입력 받고 두 숫자 사이의 합계를 구하는 코드
def add_number(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 <= num1:
        return num1
    return num2 + add_number(num1, num2 - 1)


num1 = int(input())
num2 = int(input())
print(add_number(num1, num2))