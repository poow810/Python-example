# 알파벳 같은 거 찾으려면 이중 반복문?
S = input()
count = 0
for i in S:
    for j in len(S):
        if j==i:
            count+=1


# Aaabbbbb