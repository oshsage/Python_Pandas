# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

list = list(input().split(' '))
for i in list:
    print(i);
    if i == 'q':
        break;


# i = 0
# while list[i] != 'q':
#     print(list[i])
#     i += 1


# b = []
# for i in list:
#     if i == 'q':
#         break
#     else:
#         b.append(i)
# for i in b:
#     print('%s' %i)