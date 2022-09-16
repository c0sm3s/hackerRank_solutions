def migratoryBirds(arr):
    # Write your code here
    tmpMost = 1
    most = 1
    arr = sorted(arr)
    prev = arr[0]
    vMin = arr[0]
    for b in range(1, len(arr)):
        if arr[b] == prev:
            tmpMost += 1
        else:
            if tmpMost > most:
                most = tmpMost
                vMin = prev
            tmpMost = 1
        prev = arr[b]
    if tmpMost > most:
        most = tmpMost
        vMin = prev

    return vMin   

a = [1,4,4,5,3]
a = [1, 2 ,3 ,4 ,5 ,4,3,2, 1,3,4]
a = [2, 5, 2, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 2, 2, 2, 5, 5, 1, 5, 2, 5, 5, 2, 2, 2, 2]
print(migratoryBirds(a))