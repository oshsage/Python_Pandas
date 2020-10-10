# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자. ( 1093 응용)
n = int(input());
a = input().split();
print(a)
numbers = [];

for i in range(0, n):
  numbers.append(int(a[i]));

# range에 reverse를 이용하여 숫자의 순서를 반대로 뒤집는다.
# 9부터 0까지 10번 반복한다.
for i in reversed(range(n)):
  print(numbers[i], end=' ');

