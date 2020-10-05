# 년, 월, 일을 입력받아 지정된 형식으로 출력하는 연습을 해보자.

a, b, c = input().split('.')
aa = int(a)
bb = float(b)
cc = float(c)
aaa = '%04d' % aa
bbb = '%02d' % bb
ccc = '%02d' % cc
result = str(aaa)+'.'+str(bbb)+'.'+str(ccc)
print(result)