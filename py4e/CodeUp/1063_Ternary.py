# 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

a, b = input().split(' ')
c = int(a)
d = int(b)
print(c) if c>=d else print(d)
# 새로 알게 된 것: 파이썬은 삼항연산자를 지원하지 않는다.
# [true_value] if [condition] else [false_value] // 파이썬 지원
# if문과 비슷할 수 있겠으나 뒤에 계속 이어붙이는 것이 특징이다.
# ex) bb = 1 if aa == 0 else aa