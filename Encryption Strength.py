
"""
Below is a script to compute if a certain degree of encryption can be
hacked within a given time limit. the defined function takes 3 parameters and

"""
#def encryptionValidity(instructionCount, validityPeriod, keys):
instructionCount = 1000
validityPeriod = 10000

keys = input().split()
degree = 0
keydegrees = {}
keyrepeats = {}

for key in keys:
    value = keys.count(key)
    keyrepeats[key] = value

keys = list(dict.fromkeys(keys))
for key in keys:
    count = 0
    for item in keyrepeats.keys():
        if key % item == 0:
            count += keyrepeats[item]
    keydegrees[key] = count


maxdegree = max(keydegrees.values())

encryption_strength = maxdegree * (10**5)
highjacker = instructionCount * validityPeriod

if highjacker > encryption_strength:
    highjack = 1
else:
    highjack = 0

print(keydegrees)