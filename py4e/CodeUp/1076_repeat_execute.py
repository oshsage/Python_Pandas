# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

a = input()
b = ord(a)
i=97
while i <= b:
    print(chr(i))
    i += 1