words = 'Connect Foundation'


if 'F' in words:                # 에러문이 뜨는 이유: in 표현식은 참 또는 거짓값을 반환하는 논리 표현식이며 if 구문에 사용될
    words.lower()
    words[7] = '&'
else:
    print(words)
print(words)