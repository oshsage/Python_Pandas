str = 'X-DSPAM-Confidence:0.8475'

findcolon = str.find(':')
print(findcolon)

sn = str[findcolon+1:]
print(sn)

fn = float(sn)
print(fn)

ipos = str.find(':')
piece = str[ipos+2:]
print(piece)
value = float(piece)
print(value)
