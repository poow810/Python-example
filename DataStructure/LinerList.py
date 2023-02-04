# 선형 리스트의 간단 구현

twice = ["다현", "정연", "쯔위", "사나", "지효"]  # 데이터 5개의 리스트 생성
twice.append(None)  # 리스트에 빈 칸을 추가
twice[5] = "모모"  # index 5번 자리에 데이터를 추가

twice.append(None)
twice[6] = twice[5] # 5번 자리의 데이터를 6번 자리로 옮김
twice[5] = "미나" # 빈 5번 자리에 새로운 데이터를 추가


# 선형 리스트의 일반 구현
twice = ["다현", "정연", "쯔위", "사나", "지효"]  # 데이터 5개의 리스트 생성

def insert_data(position, friend):  # 특정 위치에 데이터를 추가하는 함수

    if position < 0 or position > len(twice):
        print("data 범위를 벗어났습니다")
        return

    twice.append(None)


    for i in range(len(twice)-1, position, -1):
        twice[i] = twice[i-1]
        twice[i-1] = None

    twice[position] = friend

def del_data(position):    # 특정 위치의 데이터를 삭제하는 함수


    if position < 0 or position > len(twice):
        print("data 범위를 벗어났습니다")
        return

    twice[position] = None      # 특정 위치 데이터 삭제

    for i in range(position+1, len(twice)):
        twice[i-1] = twice[i]
        twice[i] = None     # 빈 데이터 공간을 맨 뒤로 보내기

    del(twice[len(twice)-1])    # 배열의 맨 마지막 공간 삭제

insert_data(3, "모모")
print(twice)
del_data(3)
print(twice)

