# 파일 내용 검색하기

# From: 으로 시작하는 문자열이 출력되게 한다.

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

# From: 으로 시작되는 문자열을 출력하되 오른쪽 공백 없애기.
fhand = open('mbox-short.txt')
for line in fhand :
    line.rstrip()
    if line.startswith('From:'):
        print(line)