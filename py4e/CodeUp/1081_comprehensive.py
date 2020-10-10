# 1부터 n까지, 1부터 m까지 숫자가 적힌
# 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.
# 단, n, m은 10이하의 자연수

a, b = input().split(' ')
m= int(a)
n= int(b)
if m <= 10 and n <=10:
    i = 1
    while i <= m:
        j = 1
        while j <= n:
            print(i, j)
            j +=1
        i += 1
