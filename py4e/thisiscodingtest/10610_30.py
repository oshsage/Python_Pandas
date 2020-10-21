# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에,
# 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.
# 입력: N을 입력받는다. N는 최대 10^5개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.
# 출력: 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

# 입력 숫자 리스트화
number = list(map(int,list(input())))
# 리스트 내림차순
arrange = sorted(number,reverse=True)
# print(arrange)

# 0이 아닌 수들의 배열
nonzero = []
# 0 배열
zero = []
# 리스트에서 0과 0이 아닌 숫자들을 나누기
for i in number:
    if i !=0:
        nonzero.append(i)
    else:
        zero.append(i)

# 3의 배수는 자릿수의 합이 3이므로 nonzero의 숫자의 합이 3의 배수인 것을 확인한다. (arrange로 해도 상관없음)
sum =0
for i in nonzero:
    sum += i
if sum % 3 == 0:
    result = 0
    # 3의 배수인 것이 확인되면 자릿수들을 10의 거듭제곱을 이용해 더해주어 숫자를 완성
    for i in range(len(nonzero)):
        result += nonzero[i]*10**(len(nonzero)-(i+1))
    # 자릿수 0의 경우 10의 거듭제곱을 곱해도 0이기 때문에 zero 배열에서 0의 개수를 10의 거듭제곱에 반영한다
    result *= 10**(len(zero))
print(result)