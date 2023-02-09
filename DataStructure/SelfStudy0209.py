# 11-1 최댓값 위치 찾기
def find_max_index(ary):
    maxidx = 0
    for i in range(0, len(ary)):
        if ary[i] > ary[maxidx]:
            maxidx = i
    return ary[maxidx]


array = [1, 2, 10, 50, 45, 20]
max = find_max_index(array)
print(max)