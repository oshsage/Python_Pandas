# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
#
# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D

a = int(input())
if 90<=a and a<=100:
    print("A")
elif 70<=a and a<=89:
    print("B")
elif 40<=a and a<=69:
    print("C")
elif 0<=a and a<=39:
    print("D")
else:
    print("you're failed")