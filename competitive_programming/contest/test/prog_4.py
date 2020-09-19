import math

n = int(input())
fo = []
for q in range(n):

    l = list(map(int, input().split()))
    lcm = (l[0] * l[1]) // math.gcd(l[0], l[1])
    if l[0] > l[1]:
        l[1], l[0] = l[0], l[1]
    o = []
    for i in range(l[2]):
        t = list(map(int, input().split()))
        count = 0

        if t[1] < l[1]:
            o.append(count)

        else:

            if t[0] < l[1]:
                t[0] = l[1]
            lower = (t[0] + lcm - 1) // lcm
            higher = t[1] // lcm
            m = higher - lower + 1
            last = ((t[1] // lcm) * lcm) + l[1] - 1
            value = t[1] - t[0] + 1 - m * l[1]
            # print(m, last, lcm, t[1], t[0], l[1], value)
            if last > t[1]:
                value = value + last - t[1] +1

            o.append(value)
    fo.append(o)

for i in fo:
    for j in i:
        print(j, end=' ')
    print()