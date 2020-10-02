# in을 논리 연산자로 사용하기

fruit = 'banana'

# n이 있니? -> # True로 출력됨
print('n' in fruit)
# m이 있니? -> # False로 출력됨
print('m' in fruit)
# nan이 있니? -> # True로 출력됨
print('nan' in fruit)
# 만약 a가 있다면 'Found it!'을 출력해 -> # Found it!으로 출력됨
if 'a' in fruit:
    print('Found it!')