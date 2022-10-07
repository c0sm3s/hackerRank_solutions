
def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked2 = set(ranked)
    ranked = list(ranked2)
    f = ranked[0]
    ranks = []
    group = [f]
    for s in range(1, len(ranked)):
        if ranked[s] == f:
            group.append(ranked[s])
            f = ranked[s]
        else:
            ranks.append(group)
            f = ranked[s]
            group = [f]
    ranks.append(group)

    pos = []
    added = 0
    for k in range(len(player)):
        for u in range(len(ranks)-1, -1, -1):
            if player[k] == ranks[u][-1]: 
                pos.append(u+1) # [u+1, player[k], ranks[u][-1]])
                added = 1
                break
            elif player[k] < ranks[u][-1]: 
                pos.append(u+2)
                added = 1
                break
        if added == 0: 
            pos.append(1)
        added = 0
    print(ranks)
    return pos
r = [90,70,70,60,50,50,40]
# r = [100,100,50,40,20,10]
# r = [100,90,90,80,75,60]
p = [30,50,70,90,100,10]
# p = [5,25,50,120]
# p = [50,65,77,90,102]

print(climbingLeaderboard(r,p))
