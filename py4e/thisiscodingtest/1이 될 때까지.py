
a, b = input().split()
n = int(a)
k = int(b)
# print(n, k)
cnt =0

while True:
    if n % k != 0:
        n -= 1
        cnt += 1
        if n == 1:
            break
        else:
            continue
    else:
        n /= k
        cnt += 1
        if n == 1:
            break
        else:
            continue
print(cnt)

# 동빈나 풀이
n,k = map(int, input().split())

result = 0
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k         # n과 가장 가까운 k의 배수
    result += (n-target)        # 나머지
    n = target

    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)           # n-1 의 -1은 39라인의 result +=1 과 상쇄 몫(나눈 횟수)만 더해준다.
print(result)

# 깨달은 점
# 1. map 함수는 리스트 요소에 지정된 함수로 처리하는 함수이다. 본 문제에서는 int함수를 적용해 정수로 바꿨다.
# 2. 나는 1씩 빼는 것을 반복하여 나머지를 뺀 수를 구하였지만 동빈나는 연산횟수를 고려하여 target변수로 한 꺼번에 빼는 방법을 사용
# 3. 몫은 나눈 횟수이다.