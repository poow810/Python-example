def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1), count


def is_palindrome(s):
    return recursion(s, 0, len(s)-1)

count = 0

T = int(input())
a = []
b = []
for i in range(T):
    S = input()
    a.append(is_palindrome(S))
    b.append(is_palindrome(S))

print(is_palindrome(S))