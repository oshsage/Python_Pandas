# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

a = int(input())
i = 1
sum = 0
while i <= a:
    if i % 2 ==0:
        sum += i
        i += 1
    else:
        i += 1
print(sum)

