# 개수 세기
count = 0
numbers = [9, 41, 12, 3, 74, 15]
for i in numbers:
    count = count + 1
print(count)
print('\n')

# 합 구하기
sum = 0
numbers = [9, 41, 12, 3, 74, 15]
for i in numbers:
    sum = sum + i
print(sum)
print('\n')

# 평균 구하기
sum = 0
count = 0
numbers = [9, 41, 12, 3, 74, 15]
for i in numbers:
    count = count + 1
    sum = sum + i
print('Avg: ', sum / count)
print('\n')

# 필터링하기
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    if value > 20:
        print('Large Number', value)
    else:
        print('Row Number', value)
print('\n')

# 특정값 검색하기: 3을 찾아보자
found =  False
count = 0
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    count = count + 1
    if value == 3:
        found = True
        print("I found in", count, "times.")
        break
print('\n')

# 가장 작은 수 찾기
min = None
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    if min is None:
        min = value
        continue
    elif min > value:
        min = value
print('min: ', min)
