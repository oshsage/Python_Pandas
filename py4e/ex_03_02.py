sh = input("Enter hours: ")
sr = input("Enter rate: ")

try:
    fh = float(sh)
    fr = float(sr)

except:
    print("Error")
print(fh, fr)                                   # sh: 50, sr: str 을 입력하면 fr이 존재하지 않는다고 나온다.
                                                # 그 이유는 fr에서 예외가 발생해 fr값이 없기 때문
if fh > 40:
    pay = fh * fr + (fh-40.0)*(fr*0.5)
else:
    pay = fh * fr
print("Pay: ", pay)


