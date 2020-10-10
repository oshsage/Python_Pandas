# 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

n = int(input())
a = input().split()
numbers = [];

for i in range(0, n):
  numbers.append(int(a[i]));


m=23
for i in range(n) :
    if m>numbers[i] :
        m=numbers[i]

print(m)