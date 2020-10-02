# 시작 문자열 찾기

line = 'Please have a nice day'

# Please로 시작되니? -> # True가 출력됨
print(line.startswith('Please'))
# p로 시작되니? -> # False가 출력됨 : 대소문자 구분
print(line.startswith('p'))