# 6-1 반복문 while
count = 1
while count <=5: # count값이 5보다 작거나 같을 때, 반복문 계속 실행
    print(count)
    count+=1    # count가 1씩 추가

# 6.1.1 break
while True:
    stuff = input("String to capitalize [type q to quit]")
    if stuff == "q":
        break       # 조건문 충족 시 즉시 반복문 종료
    print(stuff.capitalize())

# 6.1.2 continue
while True:
    value = input("Integer, please [q to quit]:")
    if value == 'q':    # 종료
        break
    number = int(value)
    if number % 2 ==0 :   # 짝수
        continue          # 조건문 충족시 건너뛰고 진행
    print(number, "squared is", number*number)

# 6.2 순회하기
word = 'thud'
for letter in word:
    print(letter)

# 6.2.4 숫자 시퀀스 생성 : range()
for i in range(0,3):
    print(i)