sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    # print("Overtime")
    pay = fh * fr + (fh-40.0) * (fr*0.5)

else:
    # print("Regular")
    pay = fh * fr
print('Pay: ', pay)
