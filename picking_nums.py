import math
def pickingNumbers(a):
    # Write your code here
    a = sorted(a)
    tmp = 0
    cnt = 0
    a2 = []
    ls = []
    # print(a)
    j = 0
    while len(a) > 0: # a[-1] != 0 or a[-1] != 1:
        y = 0
        cnt = 0
        a2 = []
        while y < len(a):
            tmp = abs(a[0] - a[y])
            if tmp != 0: a2.append(tmp)
            if tmp == 0 or tmp == 1: cnt += 1

            y += 1
            # print(a2)    
        a = a2
        ls.append(cnt)  
        # print("cnt", cnt)      
        
        # break
        j += 1
    # print(ls)
    return(max(ls))

def pickingNumbers2(a):
    maxCount = 1
    tempMaxCount = 1
    a = sorted(a)
    
    start = 0
    
    for i in range(1, len(a)):
        if(a[i]-a[start] > 1):
            start = i
            tempMaxCount = 1
        
        else:
            tempMaxCount += 1
            if(tempMaxCount > maxCount): maxCount = tempMaxCount
        i += 1
    
    return maxCount

def pickingNumbers3(a):
    maxi = 0
    for i in range(len(a)):
        temparr = list(a)
        for j in range(len(a)):
            temparr[j] -= a[i]
        if temparr.count(-1)>= temparr.count(1):
            possible = temparr.count(0)+ temparr.count(-1)
            if possible>= maxi:
                maxi = possible
            else:
                pass
        else:
            possible = temparr.count(0)+ temparr.count(1)
            if possible>= maxi:
                maxi = possible
            else:
                pass
    return maxi

ar = [1,1,2,2,4,4,5,5,5]
# ar = [4,6,p,3,3,1]
# ar = [1,2,2,3,1,2]
ar = [1,1,2,2,3,3,3,3]
print(pickingNumbers2(ar))
print(pickingNumbers(ar))
print(pickingNumbers3(ar))

