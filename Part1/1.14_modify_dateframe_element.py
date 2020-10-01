# coding: utf-8

import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정, df 원본객체에 변경사항 반영
df.set_index('이름', inplace=True)
print(df)
print('\n')

# 서준의 체육점수
df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
print('\n')

# 서준의 음악, 체육 점수를 모두 50으로 변경
df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')
# 서준의 음악, 체육 점수를 각각 100, 50으로 변경
df.loc['서준', ['음악', '체육']] = 100, 50
print(df)
