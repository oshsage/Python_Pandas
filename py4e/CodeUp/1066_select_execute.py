# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

list = list(input().split(' '))
for i in list:
    j = int(i)
    if j % 2 ==0:
        print("even")
    else:
        print("odd")