# 3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
# 3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.
# 10 보다 작은 정수 1개가 입력된다. (1 ~ 9)
# 입력예시: 9, 출력예시: 1 2 X 4 5 X 7 8 X

a = int(input())
if 1<=a and a<=9:
    list = []
    i = 1
    while i <= a:
        list.append(i)
        i += 1
    # print(list)
    # print(list[len(list)-1])
    for i in list:
        if i % 3 ==0:
            if i == list[len(list)-1]:
                print('X')
            else:
                print('X', end = ' ')
        else:
            if i == list[len(list)-1]:
                print(i)
            else:
                print(i, end= ' ')

# 사용한 개념: while, for, if, end. list.append
# 이번엔 end가 필수이지 않았나