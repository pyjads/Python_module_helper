import math
def c_lcm(greater, l1, l2):
    while True:
        if greater % l1 == 0 and greater % l2 == 0:
            return greater
        else:
            greater += 1

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


n = input()
l = list(map(int, input().split()))
lcm = []
for i in range(l):
    for j in range(i,l):
        greater = max(l[i],l[j])
        lcm.append(c_lcm(greater, l[i], l[j]))