# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단 0 <= a, b <= 2147483647, b는 0이 아니다.

a, b =input().split(' ')
aa = int(a)
bb = int(b)

try:
    aa >= 0
    try:
        bb != 0
        bb <=2147483647
        print(aa + bb)
        print(aa - bb)
        print(aa * bb)
        print(aa // bb)
        print(aa % bb)
        print('%.2f' % (aa / bb))

    except:
        print('error')
except:
    print('error')

# 이제는 단, 이라는 조건에 대해 try except도 걸어보자