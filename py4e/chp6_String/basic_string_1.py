# 문자열 슬라이싱

myString = 'Monty Pyton'

# Mont가 출력됩니다. 여기서 0 to 4에서 4에 대한 인덱스는 출력되는 값에 포함되지 않는 것을 확인하여야 합니다.
print(myString[0:4])
print('\n')
# P가 출력됩니다.
print(myString[6])
print('\n')
# Python이 출력됩니다.
print(myString[6:])
print('\n')
# index값이 2에 해당하는 문자 앞부터 출력됩니다.
print(myString[:2])
print('\n')
# index값이 8에 해당하는 문자부터 출력됩니다.
print(myString[8:])
print('\n')
# 전체가 출력됩니다.
print(myString[:])