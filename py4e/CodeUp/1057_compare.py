# 두 개의 참(1) 또는 거짓(0)이 입력될 때,
# 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.

a, b = input().split(' ')
if int(a) == int(b):
    if int(a)==1 or int(a)==0:
        print(1)
else:
    print(0)