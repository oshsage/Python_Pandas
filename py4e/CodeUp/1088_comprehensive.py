# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
# 3의 배수인 경우는 출력하지 않도록 만들어보자.
#
# 예를 들면,
# 1 2 4 5 7 8 10 11 13 14 ...
# 와 같이 출력하는 것이다.

a = int(input())
i = 1
list = []
while i <= a:
    if i % 3 ==0:
        i+=1
    else:
        list.append(i)
        i+=1
# print(list)
for i in list:
    if i == list[len(list)-1]:
        print(i)
        break
    else:
        print(i, end=' ')