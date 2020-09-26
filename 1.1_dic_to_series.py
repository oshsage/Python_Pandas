# -*- coding: utf-8 -*-

# pandas 불러오기

import pandas as pd

# key:value 쌍으로 딕셔너리 만들고 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로  dictionary를 Series로 변환, 변수 sr에 저장
sr = pd.Series(dict_data)

print(type(sr))         # type 함수로 객체의 자료형을 확인할 수 있다. sr의 자료형은 시리즈 클래스임을 알수 있다.
print('\n')
print(sr)               # 시리즈를 구성하는 데이터값 sr의 자료형(dtype)은 정수형(int64)이다.