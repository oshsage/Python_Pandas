# 정수(int) 2개를 입력받아 그대로 출력해보자.
a, b = input().split()
aa = int(a)
bb = int(b)
print(aa, bb)



# 새로 배운 개념: split()
# split() 함수는 괄호 안에 지정한 문자나 기호, 공백 등을 기준으로 문자를 나눈다.
# 내가 선언한 변수에 따라 문자가 나뉘므로 변수의 개수와 나눠진 단어의 개수가 맞지 않으면 에러가 뜬다.
# a, b = input().split() 으로 설정하고 print(a, b)를 했을 때, how old are you? 는 에러가 뜬다.
# 변수는 2개인데 단어는 4개로 나뉘기 때문
# a, b = input() 로 했을 때는 띄어쓰기가 용납되지 않는다. split이 없으므로 문자를 나눌수도 없다