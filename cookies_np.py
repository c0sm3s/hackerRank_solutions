from collections import deque
import time
start = time.time()

def cookies(k, A):
    A.sort()
    Aq = deque(A)
    Bq = deque()
    #print(Aq)

    if Aq[0] >= k: return 0
    if len(Aq) < 2: return -1

    cnt = 0

    while(Aq[0] < k or len(Bq) > 0):
        if len(Aq) > 0:
            if len(Bq) > 0:
                if Aq[0] >= k and Bq[0] >= k: 
                    #print("A", Aq)
                    #print("B", Bq)

                    return cnt
        #print("A: ", Aq)
        #print("B: ", Bq)
        if len(Bq) > 0:
            if Bq[0] <= Aq[0]: 
                if len(Bq) > 1:
                    if Bq[1] <= Aq[0]: 
                        #print("01")
                        val = Bq[0] + (2*Bq[1])
                        # if val > Aq[-1] and val < k: Aq.append(val)
                        if val > Aq[-1] and Aq[-1] < k: Aq.append(val)
                        elif val >= Aq[-1] and val >= k: pass
                        else: Bq.append(val)
                        Bq.popleft()
                        Bq.popleft() ## seems ok
                        
                        cnt += 1
                    else:
                        #print("02 ")
                        val = Bq[0] + (2*Aq[0])
                        if val > Aq[-1] and Aq[-1] < k: Aq.append(val)
                        elif val >= Aq[-1] and val >= k: pass
                        else: Bq.append(val)
                        Bq.popleft()
                        Aq.popleft() 
                        
                        cnt += 1
                else:
                    #print("03 ")
                    val = Bq[0] + (2*Aq[0])
                    if val > Aq[-1] and Aq[-1] < k: Aq.append(val)
                    elif val >= Aq[-1] and val >= k: pass
                    else: Bq.append(val)
                    Bq.popleft()
                    Aq.popleft() 
                    
                    cnt += 1
            elif len(A) > 1:
                
                if Bq[0] <= Aq[1]:
                    #print("04")
                    val = Aq[0] + (2*Bq[0])
                    if val > Aq[-1] and Aq[-1] < k: Aq.append(val)
                    elif Aq[-1] >= k and val >= k: pass
                    else: Bq.append(val)
                    Aq.popleft()
                    Bq.popleft() ## seems ok
                    
                    cnt += 1 
                else:
                    #print("05")
                    val = Aq[0] + (2*Aq[1])
                    if val > Aq[-1] and Aq[-1] < k: Aq.append(val)
                    elif val >= Aq[-1] and val >= k: pass
                    else: Bq.append(val)
                    Aq.popleft()
                    Aq.popleft() ## seems ok
                    
                    cnt += 1
            else: return -1
                     ## we are here **

        elif len(Aq) > 1:
            #print("06")
            val = Aq[0] + (2*Aq[1])
            if val > Aq[-1] and Aq[-1] < k: Aq.append(val)
            elif Aq[-1] >= k and val >= k: pass
            else: Bq.append(val)
            Aq.popleft()
            Aq.popleft()
            cnt += 1

        else: return -1    

        #print("Val: ", val)

        #print(Aq)
        #print(Bq)
        if(len(Aq) < 1): break

    #print("********", Aq)
    return cnt

print("cnt ", cookies(105823341, ar))
print(time.time() - start)