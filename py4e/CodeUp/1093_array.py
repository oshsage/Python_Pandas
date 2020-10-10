# 출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
# 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
# 두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

x = int(input())
el = list(input().split(' '))
array = list(range(1, 24))
# print(array)
for i in array:
    array[i-1]=0
# print(array)

for i in el:
    k = int(i)
    j=1
    while j <= 23:
        if j == k:
            # print(j)
            # print(array[j-1])
            array[j-1] = array[j-1] + 1
            # print(array[j-1])
        j += 1
# print(array)

for i in array:
    if array.index(i) == len(array)-1:
        print(i)
    else:
        print(i, end=' ')

# 새로 익힌 개념: array.index(i) == len(array)-1  -> 리스트까 끝에 도달 했다는 걸 코딩
# 10
# 9 23 1 9 23 21 11 8 18 14
