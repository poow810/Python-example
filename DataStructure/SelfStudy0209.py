# 10-2 구구단을 세로로 작성하기
def gugu_dan(dan, num):
    print(f"{dan} * {num} = {dan*num}")
    if dan < 10 :
        if num < 9:
            return gugu_dan(dan, num+1)


for i in range(2, 10):
    gugu_dan(i, 1)