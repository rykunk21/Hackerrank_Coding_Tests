"""

Given an integer, your task is to find another integer such that their
bitwise XOR is maximum.

More specifically, given the binary representation of an integer x of length n,
your task is to find another binary number y of length n with at most k set
bits such that their bitwise XOR is maximum.

For example, let's say that x = "0100" and k = 1. The maximum possible XOR can
be obtained with y = "1000", where x XOR y = "1100".

"""

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING x
#  2. INTEGER k


# Constraints
#   1 <= t <= 100
#   1 <= n <= 1000
#   0 <= k <= N

def maxXorValue(x, k):
    setbits = 0
    y = ''
    for i in range(len(x)):
        if setbits == k:
            for _ in range(len(x) - i):
                y += '0'
            break
        elif x[i] == '0':
            y += '1'
            setbits += 1
        elif x[i] == '1':
            y += '0'
    return y


if __name__ == '__main__':

    output_path = []

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        output_path.append(maxXorValue(s, k))

    for value in output_path:
        print(value)
