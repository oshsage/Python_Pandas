# 첫 번째 줄에 얼음 틀의 세로길이 N과 가로 길이 M이 주어집니다.
# 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어집니다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
# 한번에 만들 수 있는 아이스크림의 개수를 출력

# DFS 풀이

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우(x, y가 음수이거나 n, m 을 넘어설 때)에는 즉시 종료
    if x <= -1 or x >= n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] =1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)       # 상
        dfs(x, y - 1)       # 좌
        dfs(x+1, y)         # 하
        dfs(y, y+1)         # 우
        return True
        # 설명: (0,0)부터 시작해서 쫙 퍼질거임. 퍼지면서 더 나아갈수 없으면 False로 함수 종료, 계속 이어나가면 재귀로
        # 다음 노드로 퍼져나간다. 상, 하, 좌, 우를 확인하는 함수가 모두 False로 종료(함수가 모두 완료)되었을때,
        # True를 리턴하여 더이상 음료수가 퍼져나갈 수 없음을, 즉, 음료수가 하나의 덩어리가 졌음을 리턴하게 된다.
    return False




# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2 차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:                # 위의 설명대로 함수에서 True로 리턴되었을 시
            result += 1                     # 음료수 덩어리 = 아이스크림 하나 추가!

print(result)
