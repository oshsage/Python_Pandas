# 내 풀이
day = 1
sum = 0
while day <1000:
    if day % 3 ==0 or day % 5 ==0:
        sum += day
        day += 1
    else:
        day += 1
print(sum)

# 코딩도장 풀이. 추천수 79
a= sum([x for x in range(1000) if x%3==0 or x%5==0])                # range(1000):0~999까지
print(a)

# 코딩도장 풀이. 추천수 33. 집합함수 set을 처음 보는데 매우 유용해보인다.
set3 = set(range(3, 1000, 3))                                               # 3부터 999까지 3씩 뛰어서. 즉, 3의 배수
set5 = set(range(5, 1000, 5))                                               # 5부터 999까지 5씩 뛰어서. 즉, 5의 배수

print (sum(set3 | set5))


