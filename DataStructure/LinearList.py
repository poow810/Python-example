# # 선형 리스트의 간단 구현
#
# twice = ["다현", "정연", "쯔위", "사나", "지효"]  # 데이터 5개의 리스트 생성
# twice.append(None)  # 리스트에 빈 칸을 추가
# twice[5] = "모모"  # index 5번 자리에 데이터를 추가
#
# twice.append(None)
# twice[6] = twice[5] # 5번 자리의 데이터를 6번 자리로 옮김
# twice[5] = "미나" # 빈 5번 자리에 새로운 데이터를 추가
#
#
# # 선형 리스트의 일반 구현
# twice = ["다현", "정연", "쯔위", "사나", "지효"]  # 데이터 5개의 리스트 생성
#
# def insert_data(position, friend):  # 특정 위치에 데이터를 추가하는 함수
#
#     if position < 0 or position > len(twice):
#         print("data 범위를 벗어났습니다")
#         return
#
#     twice.append(None)
#
#
#     for i in range(len(twice)-1, position, -1):
#         twice[i] = twice[i-1]
#         twice[i-1] = None
#
#     twice[position] = friend
#
# def del_data(position):    # 특정 위치의 데이터를 삭제하는 함수
#
#
#     if position < 0 or position > len(twice):
#         print("data 범위를 벗어났습니다")
#         return
#
#     twice[position] = None      # 특정 위치 데이터 삭제
#
#     for i in range(position+1, len(twice)):
#         twice[i-1] = twice[i]
#         twice[i] = None     # 빈 데이터 공간을 맨 뒤로 보내기
#
#     del(twice[len(twice)-1])    # 배열의 맨 마지막 공간 삭제
#
# insert_data(3, "모모")
# print(twice)
# del_data(3)
# print(twice)
#
# # 선영 리스트의 응용 - 다항식 계산
# p = [7, -4, 0, 5]
# polyStr = "P(x) = "
# polyStr +=" + " + str(p[0]) + "x^" + str(3)
# print(polyStr)
#
#
# def printPoly(px):
#
#     term = len(px) - 1      # 최고차항 숫자 = 배열 길이 - 1
#     polyStr = "P(x) = "
#
#     for i in range(len(p)):
#         coef = px[i]        # 계수
#
#         if coef>=0:
#             polyStr +="+"
#         polyStr += str(coef) + "X^" + str(term) +" "
#         term -= 1
#
#     return polyStr
#
#
# def calcPoly(xVal, px):
#
#     retValue = 0
#     term = len(px) - 1      # 최고차항 숫자 = 배열 길이 - 1
#
#     for i in range(len(px)):
#         coef = px[i]        # 계수
#         retValue += coef * xVal ** term
#         term -= 1
#
#     return retValue
#
#
# if __name__=="__main__":
#
#     pStr = printPoly(p)
#     print(pStr)
#
#     xValue = int(input("x값 ---> "))
#     pxValue = calcPoly(xValue, p)
#     print(pxValue)

# 특수 다항식의 선형 리스트 표현
# P(x) = 7x^300-4x^20+5 --> 계수가 0인 x차수를 모조리 표현
# px= [7, 0, 0, 0,...,5] -- 301개 : 배열이 너무 많아 처리하기에 불편


# 선형 리스트 생성 함수
linear = []


def add(data):
    linear.append(None)
    size = len(linear)
    linear[size-1] = data




