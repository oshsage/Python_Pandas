# n개의 정수가 순서대로 입력된다.
# -2147483648 ~ +2147483647, 단 n의 최대 개수는 알 수 없다.
# n개의 입력된 정수를 순서대로 출력해보자.
# while( ), for( ), do~while( ) 등의 반복문을 사용할 수 없다.

cnt = int(input())
i = 1
list = list(input().split(' '))
while i < cnt+1:
    print(list[i-1])
    i += 1


# 사용한 개념: while, +=, list[n]
# list[n]: 리스트의 n번째 항. n은 0부터 시작한다!