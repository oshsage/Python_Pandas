# 파일 이름 입력 받기

# 파일의 이름을 입력 받는다. file이 열려지는 것을 try/exception 으로 걸러낸다
# 열 수 없는 파일명의 경우 'File cannot be opend:' + 파일명의 에러문 생성하고 종료
fname = input('Enter the file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opend: ', fname)
    quit()

# Subject: 로 시작하는 문자열을 받고 그 숫자를 카운팅
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        print(line)
        count = count +1
print('Count:', count)
