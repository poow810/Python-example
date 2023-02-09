# 11-2 랜덤 숫자 생성 후 내림차순 정렬
import random


def find_index(ary, num):       # 삽입될 위치 찾기
    findidx = -1
    for i in range(0, len(ary)):
        if ary[i] < num:
            findidx = i
            break
    if findidx == -1:
        return len(ary)
    else:
        return findidx


array = [random.randint(0, 200) for _ in range(10)]
after_array = []

for i in range(len(array)):
    num = array[i]
    max = find_index(after_array, num)  # after_array에 num을 담는 작업
    after_array.insert(max, num)
print(after_array)