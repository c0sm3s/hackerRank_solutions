
def formingMagicSquare(s):
    # Write your code here
    new_s = []
    i = j = 0
    
    while j < len(s[i]):
        new_s.append(s[i][j])
        j += 1
    j = 1
    i = 2
    while j < len(s):
        new_s.append(s[j][i])
        j += 1
    j = 1
    while j >= 0:
        new_s.append(s[i][j])
        j -= 1
    j = 0
    i = 1
    new_s.append(s[i][j])
    new_s.append(s[1][1])

    seq = [8,1,6,7,2,9,4,3]
    seq2 = [8,3,4,9,2,7,6,1]

    tmp = 0
    rel = []
    for we in range(int(len(seq)/2)):
        tmp = abs(s[1][1] - 5)
        for sw in range(len(seq)):
            tmp += abs(seq[sw] - new_s[sw])
        rel.append(tmp)
        seq.append(*seq[:1])
        seq.append(*seq[1:2])

        seq = seq[2:]
    for we in range(int(len(seq2)/2)):
        tmp = abs(s[1][1] - 5)
        for sw in range(len(seq2)):
            tmp += abs(seq2[sw] - new_s[sw])
        rel.append(tmp)
        seq2.append(*seq2[:1])
        seq2.append(*seq2[1:2])

        seq2 = seq2[2:]


    return min(rel)


                

arr = [[3,9,4],[7,5,5],[2,1,9]]

arr = [[2,9,8],[4,2,7],[5,6,7]]
arr = [[4,9,2],[3,5,7],[8,1,5]] # 1
arr = [[5,3,4],[1,5,8],[6,4,2]] # 7
arr = [[4,8,2],[4,5,7],[6,1,6]] # 4
arr = [[4,4,7],[3,1,5],[1,7,9]] # 20
arr = [[4,5,8],[2,4,1],[1,9,7]] # 14
print(formingMagicSquare(arr))