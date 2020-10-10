# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때,
# 압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.
#
# 예를 들어
# 일반적인 1024 * 768 사이즈(해상도)의 각점에 대해
# 24비트(rgb 각각 8비트씩 3개)로 저장하려면 1024 * 768 * 24 bit의 저장 용량이 필요하다.

a, b, c = input().split(' ')
aa = int(a)
bb = int(b)
cc = int(c)
result = aa * bb * cc /8/ 1024/1024
print('%.2f MB' % result)