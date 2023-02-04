# 5-1
# 따옴표와 문자열
# ""와 ''존재 - ""는 여러 문자열에서 유용하게 사용
# '''

# 5-4 문자열 결합
print('Release the kranken! '+'No, wait!')
vowels = ('a'"e"'''i'''"""b""")
print(vowels)
# 연산자와 괄호를 통해 문자열 결합 가능

# 5-6 문자 추출
letters = 'abcdef'
print(letters[3])

# replace와 슬라이스
name = 'Henny'
print(name.replace('H', 'P'))
print('P'+name[1:])

# 5-7 슬라이스로 부분 문자열 추출
# [:] - 처음부터 끝까지
# [start:] - start부터 끝까지
# [:end] - 처음부터 end-1까지
# [start:end] - start부터 end-1까지
# [start:end:step] - start부터 end-1까지 step씩 건너뛰면서 추출

# 5-8 문자열 길이 len()
print(len(letters))
# 문자열의 길이를 센다

# 5-9 문자열 나누기 split()
task = 'get gloves, get mask, give cat vitamins, call ambulance'
print(task.split(','))
# split(구분자) - 구분자를 기준으로 문자열을 나누어줌

# 5-10 문자열 결합하기 join()
list = ['ye', 'yee' , 'aa']
list_a = ', '.join(list)    # 구분자.join(합칠 리스트 이름)
print(list_a)   # 음.. 구분자는 공백이 상관없는건가? ', '하고 ' , '도 합쳐지네

# 5-12 문자열 스트립 strip()
world = 'aeaeasdva'
print(world.strip('e')) # 해당 문자열 모두 제거
print(world.lstrip('a')) # l, rstrip은 맨 왼, 오른쪽에 해당 문자열이 있을 시 제거

# 5-16 포매팅
# 1) 옛 스타일
actor = 'Richard Gere'
print("My wife's favorite actor is %s" % actor) # %s, %f, %d 사용 가능

# 2) 새 스타일
thing = 'woodchuck'
print('{}'.format(thing))
place = 'lake'
print('The {} is in the {}.'.format(thing, place)) # {}안에 index번호를 통해 위치 조정가능

# 3) 최신 스타일
thing = 'wereduck'
print(f'The {thing} is in the place')
