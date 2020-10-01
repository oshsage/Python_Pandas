파이썬은 파이썬 코드를 기계어로 번역하는 역할도 합니다. 번역된 기계어를 통해 대화를 하는 것입니다.

번역된 기계어를 통해 CPU와 메인 메모리가 대화하는 것.

프로그래밍을 통해 질문에 대한 답을 미리해놓는 것



에러

Traceback (most recent call last):

File "<stdin>", line 1, , in

<module>TypeError: Can't convert

'int' object to str implicityly

Traceback은 파이썬이 작동을 멈추었다는 것을 의미. 작동 중 혼란스러운 부분이 있어 더 이상 실행시키지 않았다는 것.

 이후에 error의 원인이 나온다. 위의 에러의 경우 첫번째 줄에서 <모듈> 타입 에러: 정수를 문자열로 변환할 수 없다고 함.



type() 함수는 변수의 타입을 알려줌 



숫자로된 string만 가능한 string 전환

```python
sval = '123'
type(sval)
<class 'str'>
print(sval + 1)
Traceback error가 뜰거임

# 숫자 스트링을 정수로 바꿈
ival = int(sval)
type(ival)
<class 'int'>
print(ival + 1)
124
nsv = 'hello bob'
niv = int(nsv)
Traceback error 
```



User Input

```python
nam = input('Who are you? ')
print('Welcome', nam)

결과
Who are you? osh
Welcome osh
```



파이썬은 들여쓰기(Indentation)를 잘못하면 에러가 뜨게 되어있다.

들여쓰기의 기준은 스페이스 4번

파이썬은 자바와는 달리 중괄호를 쓰지 않는 대신에 들여쓰기로 활동영역을 표시한다.



input() 함수는 무조건 string 을 반환한다.



영어에서 소문자는 대문자보다 큰 값을 갖는다... 대박이네

따라서

```python
big = max('Hello world')
-> w 
```



값을 반환하는 함수를 fruitful하다고 한다. 이유는 무언가를 생산하기 때문