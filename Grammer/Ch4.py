# Ch 4
# 4-3 if구문
# 조건 테스트가 하나일 경우
furry = True
if furry:
    print("It's a yeti")
else:
    print("It's a cat")
# furry값이 True이므로 항상 if문 반환

# 조건 테스트가 두 개 이상일 경우 - elif 구문 사용
color = "mauve"
if color == "red":
    print("tomato")
elif color == "green":
    print("watermelon")
else:
    print("...")

# 여러개 비교 - in 구문
vowels = 'aeiou'
letter = 'o'
if letter in vowels:
    print("letterm 'is a vowel'")
# 문자열뿐만 아니라 딕셔너리, 리스트에서도 멤버쉽 연산자를 사용할 수 있다.

# 바다코끼리 연산자 :=
tweet_limit = 280
tweet_string = "Blah"*50
if diff := tweet_limit - len(tweet_string): # diff = tweet_limit - len(tweet_string)을 :=로 줄여서 표현 가능
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

