count = 0
sum = 0
while True:
    sn = input('Enter the number: ')
    if sn != 'done':
        try:
            fn = float(sn)
        except:
            print('bad data')
            continue
        count = count + 1
        sum = sum + fn

    elif sn == 'done':
        break
print('Count: ', count)
print('\n')
print('Sum: ', sum)
print('\n')
avg = sum / count
print('Avg: ', avg)



