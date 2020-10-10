# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.


list = list(input().split(' '))
for i in list:
    j = int(i)
    if j % 2 ==0:
        print(j)
    else:
        continue

# 사용한 개념: list, for, if, continue