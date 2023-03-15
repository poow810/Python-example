dest = input("택배가 배송될 지역을 알려주세요 : ")
if dest == "부산":
    dest_cost = 4600
elif dest == "울산":
    dest_cost = 4300
elif dest == "인천":
    dest_cost = 2000
elif dest == "강원":
    dest_cost = 3100
elif dest == "전북":
    dest_cost = 2700
else:
    pass

weight = int(input("택배의 무게를 알려주세요. 단위는 g입니다. : "))
if weight < 1000:
    weight_cost = 0
elif 1000 <= weight < 2500:
    weight_cost = 1000
elif 2500 <= weight < 5000:
    weight_cost = 2500
else:
    weight_cost = (weight // 1000) * 1000

ship_cost = dest_cost + weight_cost
while True:
    ship = int(input("택배 유형을 알려주세요. 0은 일반, 1은 특급, 2는 퀵입니다. : "))
    if ship == 0:
        ship_cost = ship_cost
        break
    elif ship == 1:
        ship_cost = ship_cost * 1.25
        break
    elif ship == 2:
        ship_cost = ship_cost * 5
        break
    else:
        print("메뉴에서 선택하여 주세요")

cost = int(ship_cost)
print(cost)
print(f"최종 택배 비용은 다음과 같습니다 : {cost}")
