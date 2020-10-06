


color = input()
w = 0
b = 0
wendy = 0
bob = 0


for let in color:
    if let == 'w':
        b = 0
        w += 1
    elif let == 'b':
        w = 0
        b += 1
    if w >= 3:
        wendy += 1
    elif b >= 3:
        bob += 1
    else:
        continue

if wendy > bob:
    print('Wendy')
elif bob >= wendy:
    print('Bob')
