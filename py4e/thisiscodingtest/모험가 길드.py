#
# n = int(input())
# adventure = list(input().split())
# numbers = list(range(1,n+1))
# print(numbers)
# seq = list()
# for i in numbers:
#     x = int(i)
#     for j in adventure:
#         y = int(j)
#         if x == y:
#             seq.append(y)
#         else:
#             continue
# print(seq)
#
# cnt = 0
# for i in seq:
#     x = int(i)
#     if n >= x:
#         n -= n//x * x
#         cnt += 1
#     else:
#         break
# print(cnt)

# 동빈나 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data)

result = 0  # 총 그룹의 수
count = 0   # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하여
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면 그룹 결성
        result +=1  # 총 그룹의 수 증가
        count = 0   # 그룹이 된 사람을 보내고 다음 사람을 불러오기 위해 그룹안에 사람을 비운다.
print(result)


# 깨달은점
# 1. 젠장 sort라는 함수를 몰랐다... sort는 리스트를 오름차순으로 정렬시키는 함수이다.
# 2. 애초에 생각이 달랐다. 나는 전체 수를 깎고 횟수를 그륩수로서 구하려했지만 동빈나는 그륩이라는 공간안에서 시작하여
# 그륩 속에 사람을 한명씩 넣으면서 공포도를 계량하는 방식이다. 마치 신체검사를 받는 듯 프로그래밍을 하였다.