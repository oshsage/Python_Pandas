# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

a, b = input().split(' ')
aa = int(a)
bb = int(b)
try:
    0<=aa & aa<=10
    0<=bb & bb<=10
    print(aa*2**bb)
except:
    print('error')