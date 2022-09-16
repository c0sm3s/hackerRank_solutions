
import math

def getTotalX(a, b):
    # Write your code here
    a_max = max(a)
    b_min = min(b)
    factors = []
    tmp1 = set()
    tmp2 = set()

    for x in range(len(a)):
        start = math.ceil(a_max/a[x])
        stop = math.ceil(b_min/a[x])
        tmp1 = set()
        for i in range(start, stop + 1):
            tmp1.add(a[x] * i)
        if x == 0:
            tmp2 = tmp1
        else:
            tmp2 = tmp2.intersection(tmp1)
    tmp2 = list(tmp2)
    for z in range(len(tmp2)):
        for j in range(len(b)):
            if b[j]%tmp2[z] != 0:
                break
            if j == len(b) - 1:
                factors.append(tmp2[z])
    return(len(factors))



a = [2, 4]
a = [2, 6]
b = [16, 32, 96]
b = [24, 36]
print(getTotalX(a, b))