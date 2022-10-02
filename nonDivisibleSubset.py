
def nonDivisibleSubset(k, s):
    # Write your code here
    s2 = [(i%k) if i%k != 0 else k for i in s]
    res = []
    tmp = []
    nums = []
    cnt = 0

    # for j in range(len(s2)-1):
    #     cnt = 0
    #     for l in range(j+1, len(s2)):
    #         # print("s2[j] + s2[k]", s[j], s[l], s2[j] + s2[l])
    #         if (s2[j] + s2[l]) % k == 0:
    #             cnt += 1
    #             # print(cnt)
    #     res.append(cnt)
    #     # print("next")


    print((s2),"con len =", len(s)) # sorted
    print(sorted(s2))
    s3 =  sorted(s2)
    if len(s3) == 0: return len(s)
    y = 0
    val1 = s3[0]
    cnt1 = 0
    pos1 = 1
    cnt2 = 0
    pos2 = 0
    val2 = 0
    comp = 0
    s_len = len(s)
    while True:
        print("************************")
        pos1 = 0
        curVal = s3[pos1]
        cnt1 = 0
        avoidComp = 0
        # pos2 = pos1 + 1
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
        # if s3[0] == k: s_len -= (len(s3) - (len(s3) - 1))
    # if s3[-1] == k: add something

    
    return s_len

kk = 5
ss = [16,2,7,5,10,3,6]
ss = [1,7,2,4] # k = 3, 3
ss = [5,0,5] # k = 5, 1
ss = [16,67,3,4,0,9] # k = 4, 3
ss = [14,7,3,90,26,4]

ss = [19,10,12,24,25,22] # k = 4, 3
ss = [3,6,9,68] # k = 4, 3
ss = [2,10,13,17,21,9] # k = 5, 4
ss = [3,7,9,2,45,55,15,855,234905,0,6,67] # k = 5, 5
ss = [45,55,15,855,234905] # k = 5, 1


print(nonDivisibleSubset(kk, ss))