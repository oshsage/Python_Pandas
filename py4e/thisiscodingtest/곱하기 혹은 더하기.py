list = map(int, list(input()))
print(list)
result = 0
for i in list:
    if result == 0:
        result += i
    else:
        if i !=0 or i !=1 :
            result *= i
        else:
            result += i
print(result)

# 동빈나 풀이
data = input()
# 첫 번째 문자를 숫자로 변경하여 기입(기준으로 잡겠다)
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <=1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

# 인사이트
# 1. 첫번째 result는 첫번째 원소를 기준으로 잡기 위해 그랬다
# 2. 이전 문제에서 map 써서 따라했더니 여기서는 안 쓴다. 하지만 답이 한가지는 아니니까 패스
# 3. 자릿수가 소수가 나올리가 없기 때문에 나는 i !=0 or i !=1 로 0과 1을 지정했지만 동빈나는 부등호로 실수도 고려했다.