
# 5
# 5 3
# 1 5 2 6 1
# 1 6
# 6
# 3 2
# 1 2 3
# 4 3
# 3 1 2 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10

i = int(input())
l = []
for j in range(i):
    k = list(map(int,(input().split(' '))))

    il = list(map(int,input().split(' ')))
    if k[1] in il and len(il)==1:
        l.append('yes')
    elif k[1] in il[1:] and len(il) % 2 == 1:
        l.append('yes')
    elif k[1] in il[1:-1] and len(il) % 2 == 0:
        l.append('yes')
    else:
        l.append('no')

for t in l:
    print(t)
