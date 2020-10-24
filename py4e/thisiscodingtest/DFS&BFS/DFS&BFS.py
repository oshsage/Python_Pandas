# 스택 자료 구조
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()         # 리스트의 맨 마지막 요소를 돌려주고 그 요소를 삭제 (가장 나중에 드러온 7이 삭제)
stack.append(1)
stack.append(4)
stack.pop()         # 가장 최근 숫자 4가 삭제

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)        # 최하단 원소부터 출력

#----------------------------------------------------------------------------------------------------------------------
# 큐 자료 구조

from collections import  deque
# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)     # 원소를 삽입
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()     # 가장 왼쪽에 있는 원소를 꺼내어 삭제. 여기서는 가장 먼저 들어간 5가 삭제
queue.append(1)
queue.append(4)
queue.popleft()     # 두 번째로 들어갔던 2가 삭제

print(queue)        # 먼저 들어온 순서대로 출력
queue.reverse()     # 역순으로 바꾸기
print(queue)        # 나중에 들어온 원소부터 출력

#----------------------------------------------------------------------------------------------------------------------
# 재귀 함수

# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()

# 재귀 함수 종료 조건
def recursive_function(i):
    # 100번째 호출으 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')         # 스택 자료처럼 가장 나중에 출력 i를 기준으로 프린트 출력

recursive_function(1)

# 팩토리얼 구현 예제
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1);

print('재귀적으로 구현:', factorial_recursive(5))		# 출력값 120

# 최대공약수 계산(유클리드 호제법)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a % b)
print(gcd(192,162))             # 출력값 6

#----------------------------------------------------------------------------------------------------------------------
# DFS 소스코드 예제

# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True                   # v번 노드에 방문했습니다.
    print(v, end =' ')                  # 방문했다고 출력
    for i in graph[v]:                  # graph[v]는 v번 노드와 인접한 노드배열을 의미
        if not visited[i]:              # if not 조건: 조건이 거짓일 때 수행. 예를 들어 visited[2]가 False이면 밑에 dfs 함수 실행
            dfs(graph, i, visited)      # 해석하면  v번 노드와 인접한 노드중 가장 작은 수의 노드가 거짓(False = 방문 x)이라면 dfs 함수 실행(
                                        # 방문하지 않았은 노드를 방문하겠다라는 의미

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],             # 배열의 첫번째가 0부터 시작하기 때문에 1번노드가 배열[1]이 1번노드가 될수 있게 배열[0]을 비워놓는다.
    [2, 3, 8],      # 1번 노드의 인접 노드들
    [1, 7 ],        # 2번 노드의 인접 노드들
    [1, 4, 5],      # 3번 노드의 인접 노드들
    [3, 5],         # 4번 노드의 인접 노드들
    [3, 4],         # 5번 노드의 인접 노드들
    [7],            # 6번 노드의 인접 노드들
    [2, 6, 8],      # 7번 노드의 인접 노드들
    [1, 7],         # 8번 노드의 인접 노드들
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)          # 출력값 1 2 7 6 8 3 4 5

#----------------------------------------------------------------------------------------------------------------------
# BFS 소스코드 예제

# from collections import deque (위에 코드에서 이미 써서 여긴 주석처리함)

def bfs(graph, start, visited):
    queue = deque([start])                  # 큐 구현을 위해 deque 라이브러리 사용
    visited[start] = True                   # 현재 노드를 방문 처리
    while queue:                            # 큐가 빌 때까지 반복
        v =queue.popleft()                  # 현재 노드를 꺼내고 v에 저장 (한 바퀴 돌았을 때부터는 i번 노드를 꺼내어 v에 저장했다고 보면 되겠지?)
        print(v, end = ' ')                 # 출력
        for i in graph[v]:                  # v번 노드와 인접한 노드배열 중 가장 작은수 부터 방문하러
            if not visited[i]:              # v번과 인접한 노드 i가 거짓(False = 방문 x)이라면
                queue.append(i)             # 큐에 해당 노드를 추가
                visited[i] = True           # i번 노드 방문 처리

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],             # 배열의 첫번째가 0부터 시작하기 때문에 1번노드가 배열[1]이 1번노드가 될수 있게 배열[0]을 비워놓는다.
    [2, 3, 8],      # 1번 노드의 인접 노드들
    [1, 7 ],        # 2번 노드의 인접 노드들
    [1, 4, 5],      # 3번 노드의 인접 노드들
    [3, 5],         # 4번 노드의 인접 노드들
    [3, 4],         # 5번 노드의 인접 노드들
    [7],            # 6번 노드의 인접 노드들
    [2, 6, 8],      # 7번 노드의 인접 노드들
    [1, 7],         # 8번 노드의 인접 노드들
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)          # 출력값 1 2 3 8 7 4 5 6