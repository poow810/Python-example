n = int(input())
for i in range(n):
    word_list = list(input())
count = 0
for i in range(len(word_list) - 1):
    for j in word_list:
        if word_list[i] == word_list[i + 1]:
            pass
        elif word_list[i] in word_list[i + 1]:
            count -= 1
print(n - count)
# case 1 : 중복되는 문자열이 없으면 그룹 단어
# case 2 : 문자열이 1개나, 종류가 한 가지일 때, 그룹 단어
#
