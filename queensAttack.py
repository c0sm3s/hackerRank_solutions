def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    movs = 0
    board = [[" " for i in range(n)] for j in range(n)]

    for a in range(n):
        if a != c_q -1: board[r_q-1][a] = "1"
        if a != r_q -1: board[a][c_q-1] = "1"

    row_start = col_start = 1
    if r_q > c_q: 
        row_start = r_q - (c_q - 1)
    else:
        col_start = c_q - (r_q - 1) 
    

    while row_start <= n and col_start <= n:
        board[row_start-1][col_start-1] = "1"
        row_start += 1
        col_start += 1


    c_q2 = (n - c_q) + 1
    print(c_q2)
    row_start = 1
    col_start = 7
    if r_q > c_q2: 
        row_start = r_q - (c_q2 - 1)
    else:
        col_start = c_q2 - (r_q - 1) 
        col_start = n - (col_start  - 1 )

    print(row_start, col_start)
    while row_start <= n and col_start >= 1:
        board[row_start-1][col_start-1] = "1"
        row_start += 1
        col_start -= 1


    for i in obstacles:
        f, c = i
        if board[f-1][c-1] ==  "1": board[f-1][c-1] = "x"

    board[r_q-1][c_q-1] = "Q"
    
    
    for t in board:
        print(t)

    return movs


nn = 7
obs = [[1,1],[2,3],[7,7],[3,6],[3,2]]
kk = len(obs)
rq = 3
cq = 4
print(queensAttack(nn,kk,rq,cq,obs))