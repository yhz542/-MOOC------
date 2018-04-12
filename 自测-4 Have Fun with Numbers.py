N = input()
L = [ 0 for i in range (10) ]
for i in N :
    L[ int( i ) ] += 1
N = int( N ) * 2
N = str( N )
for i in N :
    L[ int( i ) ] -= 1
flag = 0
for i in L:
    if i:
        flag = 1
        break
if flag:
    print('No')
else :
    print('Yes')
print( N )
