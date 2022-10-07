
def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    movs = 0
    cols = []
    board = []

    board = [[1 for i in range(n)] for j in range(n)]
    # for r in range(n):
    #     board.append(cols)

    for i in range(n):
        board[i][i] = 0
        print(board[i])
 
    
    
    # for t in board:
    #     print(t)
    print(board)

    return movs


nn = 5
obs = [[1,1],[2,3]]
kk = len(obs)
rq = 3
cq = 3
print(queensAttack(nn,kk,rq,cq,obs))