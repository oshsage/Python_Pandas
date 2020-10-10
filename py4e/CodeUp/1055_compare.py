# 두 개의 참(1) 또는 거짓(0)이 입력될 때,
# 하나라도 참이면 참을 출력하는 프로그램을 작성해보자.

a, b = input().split(' ')
if int(a)==1 or int(b)==1:
    print(1)
else:
    print(0)