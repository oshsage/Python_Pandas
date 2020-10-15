for i in range(5):
    for j in range(5):
        print('(',i,',',j,')', end = ' ')
    print()

# 1. 행렬은 기본적으로 좌측 상단이 (0,0)으로 시작한다.
# 2. range(n)은 0부터 n개 라는 소리. 즉, 0~(n-1) 이다.
# 3. 마지막에 print() 가 없다면 요소들이 쭉 이어붙는다. print()는 행과 행을 구분하는 함수

#     동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    # 다음 위치 (반 시계방향으로 출력. 동-> 북-> 서-> 남)
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)