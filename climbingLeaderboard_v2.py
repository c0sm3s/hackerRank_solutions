from collections import deque
import tc
def climbingLeaderboard(ranked, player):
    # Write your code here RANKED = SCORES -- PLAYER = SCORE PLAYER
    ppos = 0
    pos = []
    ranked = list(dict.fromkeys(ranked))
    u = len(ranked) - 1
    while u >= 0:
        if ranked[u] == player[ppos]:
            pos.append(u+1)
            ppos += 1
            u += 1
        elif ranked[u] > player[ppos]:
            pos.append(u+2)
            ppos += 1
            u += 1
        if ppos == len(player): break
        u -= 1
    if ppos < len(player):
        pos += [1 for i in range(len(player) - ppos)]

    return pos
r = [90,70,70,60,50,50,40]
r = [100,100,50,40,20,10]
r = [90,90,80,75,60]
p = [30,50,70,90,100,10]
p = [5,25,50,120]
p = [50,65,77,90,90]

print(climbingLeaderboard(r,p))