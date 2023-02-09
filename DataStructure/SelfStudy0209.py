# 12-1 랜덤하게 숫자 생성 후 내림차순으로 정렬, 그 횟수를 세기
import random
def quick_sort(ary):
    global count
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n//2]
    left_array, right_array = [], []

    for num in ary:
        if num > pivot:
            right_array.append(num)
        elif num < pivot:
            left_array.append(num)
    count += 1
    return quick_sort(right_array) + [pivot] + quick_sort(left_array)


array = [random.randint(0, 200) for _ in range(20)]
count = 0
print(quick_sort(array))
print(count)