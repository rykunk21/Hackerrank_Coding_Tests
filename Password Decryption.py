
s = '51Pa*0Lp*0e'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
nums = '123456789'
decode = []
beginnums = []

cursor = 1
for i in range(len(s)):
    try:
        if s[i+2] == '*':
            continue
        elif s[i+1] == '*':
            continue
    except IndexError:
        if s[i] == '*':
            decode.append(s[i - 1])
            decode.append(s[i - 2])
            continue
        if s[i] == '0':
            decode.append(beginnums[0])
            beginnums.pop(0)
            continue
        else:
            decode.append(s[i])
            continue
    if s[i] == '*':
        decode.append(s[i-1])
        decode.append(s[i-2])
        continue
    if s[i] in nums:
        beginnums.insert(-1, s[i])
        continue
    if s[i] == '0':
        decode.append(beginnums[0])
        beginnums.pop(0)
    else:
        decode.append(s[i])
finstr = ''
for i in decode:
    finstr += i

print(finstr)

