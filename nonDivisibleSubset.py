
def nonDivisibleSubset(k, s):
    # Write your code here
    s3 = [(i%k) if i%k != 0 else k for i in s]
    s3 = sorted(s3)

    s4 = []
    total_len = len(s)
    f = s3[0]
    group = [f]
    for v in range(1, len(s3)):
        if s3[v] == f:
            group.append(s3[v])
            f = s3[v]
        else:
            s4.append(group)
            f = s3[v]
            group = [f]
    s4.append(group)

    p1 = 0
    v1 = s4[p1]
    
    while len(s4) > 1:
        v1 = s4[0]
        q = 1
        while q < len(s4) and (s4[q][0] + v1[0]) <= k:
            if v1[0] == k/2 or v1[0] == k: 
                total_len -= len(s4[0]) - 1
                break
            if (v1[0] + s4[q][0])%k == 0:
                print("MATCH")
                if len(s4[q]) > len(v1): total_len -= len(v1)
                else: total_len -= len(s4[q])
                del s4[q]
                break
            q += 1
        del s4[0]
        print("----",s4,"----",total_len)
        p1 += 1
    # print("v1!",v1)
    if len(s4) > 0 and (s4[0][0] == k/2 or s4[0][0] == k): total_len -= len(s4[0]) - 1

    print("RESULT 01 ===> ", total_len, "\n\n")

    print(s4)


    print((s3),"con len =", len(s)) # sorted
    # print(sorted(s3))
    # s3 =  sorted(s2)
    cnt1 = 0
    pos1 = 1
    cnt2 = 0
    pos2 = 0
    comp = 0
    s_len = len(s)
    while True:
        print("************************")
        pos1 = 0
        curVal = s3[pos1]
        cnt1 = 0
        avoidComp = 0
        while True:
            cnt1 +=1
            curVal = s3[pos1]
            pos1 += 1
            
            if pos1 == len(s3) or s3[pos1] != curVal: break
        comp = k - curVal
        if curVal == k/2 and cnt1 > 1:
            s_len -= (cnt1 - 1)
            avoidComp = 1
        elif curVal == k and cnt1 > 1:
            s_len -= (cnt1 - 1) # (len(s3) - 1)
            print("LLEGAMOS A K")
            avoidComp = 1

        print("cnt1", cnt1, curVal, pos1)

        s3 = s3[pos1:]
        cnt2 = 0

        if len(s3) > 0 and avoidComp == 0:
            pos2 = 0
            curVal2 = s3[pos2]
            while True:
                if s3[pos2] == comp:
                    cnt2 += 1
                    curVal2 = s3[pos2]
                pos2 += 1
                if pos2 == len(s3) or (s3[pos2] != curVal2 and cnt2 > 0):
                    break
            
            print("cnt2", cnt2, curVal2, pos2)
            s3 = s3[:pos2-cnt2] + s3[pos2:]
            print("2nd while", s3)
        
        if cnt2 > 0 and cnt2 < cnt1:
            s_len -= cnt2
        elif cnt2 > 0: 
            s_len -= cnt1

        print("LEN S",s_len)

        if len(s3) == 0: break
    return s_len

kk = 7
ss = [1,7,2,4] # k = 3, 3
# ss = [5,0,5] # k = 5, 1
# ss = [16,67,3,4,0,9] # k = 4, 3
# ss = [14,7,3,90,26,4] # k = 4, 4

# ss = [19,10,12,24,25,22] # k = 4, 3
# ss = [3,6,9,68] # k = 4, 3
# ss = [2,10,13,17,21,9] # k = 5, 4
# ss = [3,7,9,2,45,55,15,855,234905,0,6,67] # k = 5, 5
# ss = [45,55,15,855,234905] # k = 5, 1

# ss = [14,6,8]
# ss = [16,2,7,5,10,3,6]
# ss = [2,7,2,6,23,67,35,754,12,235,2235,843,23,346,2,6346,2235,646]
ss =[278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
ss = [0,1,7]

print(nonDivisibleSubset(kk, ss))