# 7.1 튜플
one_tuple = ()
two_tuple = 'a',
three_tuple = ('a',)

# 튜플 언패킹
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
# password : 'tuttifrutti' / icecream : 'swordfish'

# 리스트 -> 튜플
one_list = ['A', 'B', 'C']
print(tuple(one_list))

# 7.2 리스트
a_list = []
b_list = list()
print(list('cat'))      # 문자열을 리스트로 변환

# 7.2.3 문자열 분할로 생성 : split()
day = '9/19/2019'
print(day.split('/'))

# 7.2.4 [offset]으로 항목 얻기
list_a = ['a', 'b', 'c']
print(list_a[0])

# 7.2.5 슬라이스로 항목 얻기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])

# 7.2.6 리스트 끝에 항목 추가 : append
marxes.append('a')
print(marxes)

# 7.2.7 offset과 insert로 항목 추가
marxes.insert(3, 'b')
print(marxes)

# 7.2.9 리스트 병합 : extend
a = ['a']
b = ['b']
a.extend(b)
print(a)

# 7.2.10 offset, slice로 항목 변경
a = ['a', 'b', 'c']
a[2] = 'd'
print(a)

b = ['1', '2', '3']
b[0:1] = ['4', '5']
print(b)

# 7.2.12 항목 삭제하기
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
del marxes[-1]      # del : [-1]위치의 항목 삭제
print(marxes)
marxes.remove('Harpo')    # remove : 해당 문자열 삭제
marxes.pop()        # pop() : 해당 offset 위치한 요소 삭제 기본값 -1

# 7.2.19 문자열로 변환
marxes = ['a', 'b', 'c']
marxe = ', '.join(marxes)
print(marxe)

# 7.2.22 리스트 할당
a = [1, 2, 3]
b = a
a[0] = 4        # 여러 변수에 리스트를 할당하면 한 리스트 변경 시 다른 리스트도 변경
# b --> [4, 2, 3]
