# for i in range(1,101):
#     for j in range(1,101):
#         print('(',i,',',j,')', end=' ')
#     print()
# r = x + dx[0]
# u = y + dy[1]
# l = x + dx[2]
# d = y + dy[3]

x, y = 1, 1

dx= [0, -1, 0, 1]
dy= [1, 0, -1, 0]


n = int(input())
go = list(input().split())

for i in go:
    if i == 'R':
        y += dy[0]
        if y > n:
            y -= dy[0]
    elif i == 'U':
        x += dx[1]
        if x < 1:
            x -= dx[1]
    elif i == 'L':
        y += dy[2]
        if y < 1:
            y -= dy[2]
    elif i == 'D':
        x += dx[3]
        if x > n:
            x -= dx[3]
print(x, y)

# 동빈나 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우는 무시
    if nx < 1 or ny < 1 or nx >n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)

# 깨달은 점
# 1. 개념에 나온 코드들을 어떻게 사용하는지 알려준 풂이였다. 나도 풀었지만 1차원적이고 줄이 길다.
# 2. 공간을 벗어나는 경우 무시하는 코드가 기발하다. 안에서 nx, ny 변수를 생성하고 continue로 넘겨 nx, ny 값을 저장하지 않는 방식
