def solve(A):
    A = sorted(A)

    curV = None
    for i in range(len(A)):
        if i == 0:
            curV = A[i]
        elif curV != A[i]:
            if i == (len(A) - 1):
                if A[i] == 0:
                    return 1
            if len(A) - i == curV:
                return 1
            curV = A[i]
        elif i == (len(A) - 1):
            if A[i] == 0:
                return 1

    return -1

def wave(A):
    A = sorted(A)
    i = 0
    while i < len(A):
        if i != (len(A) - 1):
            temp = A[i]
            A[i] = A[i + 1]
            A[i + 1] = temp
        i = i + 2
    return A


def compa(n1, n2):
    n1 = str(n1)
    n2 = str(n2)

    print n1, " ", n2

    curn1 = None
    curn2 = None

    k2 = 0
    k1 = 0
    for i in range(max(len(n1), len(n2))):
        fl1 = False
        fl2 = False
        if i < len(n1):
            fl1 = True
            curn1 = int(n1[i])
        if i < len(n2):
            fl2 = True
            curn2 = int(n2[i])

        if curn1 != curn2:
            if fl1 and fl2:
                print str(curn1 - curn2)
                return curn1 - curn2
            elif not fl1:
                k1 = k1 + curn1
                k2 = k2 + curn2
                if curn2 > curn1:
                    print str(-1)
                    return -1
            elif not fl2:
                k2 = k2 + curn2
                k1 = k1 + curn1
                if curn1 > curn2:
                    print str(1)
                    return 1

    if curn1 == curn2:
        print str(k1-k2)
        return k1 - k2

    print str(curn1-curn2)
    return curn1 - curn2


a = [ 782, 240, 409, 678, 940, 502, 113, 686, 6, 825, 366, 686, 877, 357, 261, 772, 798, 29, 337, 646, 868, 974, 675, 271, 791, 124, 363, 298, 470, 991, 709, 533, 872, 780, 735, 19, 930, 895, 799, 395, 905 ]

# a = sorted(a, cmp=compa)

A = 3
centre = A - 1
for i in xrange(A+A-1):
    for j in xrange(A+A-1):
        print max(abs(i-centre), abs(j-centre)) + 1,
    print ""