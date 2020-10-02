# 파워 핸들

fhand = open('mbox-short.txt')

for line in fhand:
    print(line)

# 파일 라인 수 세기
fhand = open('mbox-short.txt')
count=0

for line in fhand:
    count = count + 1
print('Count: ', count)

# 파일 전체 읽기: 파일 전체 내용을 불러오고 그중 20번째 문자까지 출력
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])