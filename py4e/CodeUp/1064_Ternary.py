# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

a, b, c = input().split(' ')
d = int(a)
e = int(b)
f = int(c)
print(d) if d<=e and d<=f else (print(e) if e<=d and e<=f else print(f))