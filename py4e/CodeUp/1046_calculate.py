# 정수 3개를 입력받아 합과 평균을 출력해보자.
# 단, -2147483648 ~ +2147483647

a, b, c = input().split(' ')
sum = int(a)+int(b)+int(c)
avg = sum/3
print(sum)
print('%.1f' % avg)