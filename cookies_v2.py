import time
start = time.time()
# def get_mins(cookies):
#     return sorted(cookies)
    # return cookies[0], cookies[1]

def cookies(k, A):
    # A = sorted(A)
    A.sort()

    if len(A) < 2 and A[0] < k: return -1
    if A[0] >= k: return 0

    B = []    
    cnt = 0
    # last_val = A[len(A)-1]

    while(A[0] < k or len(B) > 0):
        if len(A) > 0:
            if len(B) > 0:
                if A[0] >= k and B[0] >= k: 
                    print("A", A)
                    print("B", B)

                    return cnt
        print("A: ", A)
        print("B: ", B)
        if len(B) > 0:
            if B[0] <= A[0]: 
                if len(B) > 1:
                    if B[1] <= A[0]: 
                        print("01")
                        val = B[0] + (2*B[1])
                        # if val > A[len(A)-1] and val < k: A.append(val)
                        if val > A[len(A)-1] and A[len(A)-1] < k: A.append(val)

                        elif val >= A[len(A)-1] and val >= k: pass

                            
                        # if val > A[len(A)-1]: 
                        #     A.append(val)
                        else: B.append(val)
                        B.pop(0)
                        B.pop(0) ## seems ok
                        
                        cnt += 1
                    else:
                        print("02 ")
                        val = B[0] + (2*A[0])
                        # if val > A[len(A)-1]: A.append(val)
                        # if val > A[len(A)-1] and val < k: A.append(val)
                        if val > A[len(A)-1] and A[len(A)-1] < k: A.append(val)

                        elif val >= A[len(A)-1] and val >= k: pass
                        else: B.append(val)
                        B.pop(0)
                        A.pop(0) 
                        
                        cnt += 1
                else:
                    print("03 ")
                    val = B[0] + (2*A[0])
                    # if val > A[len(A)-1]: A.append(val)
                    # if val > A[len(A)-1] and val < k: A.append(val)
                    if val > A[len(A)-1] and A[len(A)-1] < k: A.append(val)

                    elif val >= A[len(A)-1] and val >= k: pass
                    else: B.append(val)
                    B.pop(0)
                    A.pop(0) 
                    
                    cnt += 1
            elif len(A) > 1:
                
                if B[0] <= A[1]:
                    print("04")
                    val = A[0] + (2*B[0])
                    # if val > A[len(A)-1]: A.append(val)
                    # if val > A[len(A)-1] and val < k: A.append(val)
                    if val > A[len(A)-1] and A[len(A)-1] < k: A.append(val)

                    elif A[len(A)-1] >= k and val >= k: pass
                    else: B.append(val)
                    A.pop(0)
                    B.pop(0) ## seems ok
                    
                    cnt += 1 
                else:
                    print("05")
                    val = A[0] + (2*A[1])
                    # if val > A[len(A)-1]: A.append(val)
                    # if val > A[len(A)-1] and val < k: A.append(val)
                    if val > A[len(A)-1] and A[len(A)-1] < k: A.append(val)

                    elif val >= A[len(A)-1] and val >= k: pass
                    else: B.append(val)
                    A.pop(0)
                    A.pop(0) ## seems ok
                    
                    cnt += 1
            # elif len(A) > 1:
                # if B[0] <= A[1]:
                
            else: return -1
                     ## we are here **
                        


                # sec = A[1]
                # 

        elif len(A) > 1:
            print("06")
            val = A[0] + (2*A[1])
            # if val > A[len(A)-1]: A.append(val)
            if val > A[-1] and A[-1] < k: A.append(val)
            # elif val >= A[len(A)-1] and val >= k: pass
            elif A[-1] >= k and val >= k: pass

            else: B.append(val)
            A.pop(0)
            A.pop(0)
            
            cnt += 1

        else: return -1    

        # A.pop(0)
        
        print("Val: ", val)

        print(A)
        print(B)
        if(len(A) < 1): break


    #         if val < k: B.append(val)
    #         else: A.append(val)
    #         # A = get_mins(A)
    #         cnt += 1
    #     A = get_mins(A)
    # if A[0] < k: return -1 
    print("********", A)
    return cnt
        
ar = [1,4,13,5,6,8,2,3,9,10,12,7,3,9,2,52, 34, 13, 37]
# ar = [1,1,1,2,2,3,7,8,9]




print("cnt ", cookies(615787220, ar))
print(time.time() - start)