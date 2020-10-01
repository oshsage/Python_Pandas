def computerpay(hours, rate):
    # print("in compute pay", hours, rate)
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp

    else:
        pay = hours * rate
    #print("Returning: ", pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

# 40시간 초과근무시 5할 가산 지급
pay = computerpay(fh, fr)

print("Pay: ", pay)
