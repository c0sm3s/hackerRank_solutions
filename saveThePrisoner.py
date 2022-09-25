def saveThePrisoner(n, m, s):
    # Write your code here
    st = s - 1
    i = n - st
    j = m - i
    x = j//n
    z = j%n
    if i <= 0: 
        return n - abs(j)
    if z == 0: 
        return n
    return z

i = 654809340  
j = 204894365
k = 472730208
# i = 8 
# j = 50
# k = 4

print(saveThePrisoner(i,j,k))