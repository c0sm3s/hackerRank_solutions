
def surfaceArea(A):
    # Write your code here
    print(A)
    total = 0
    for rows in range(len(A)):
        tmp = 0
        for cols in range(len(A[rows])):
            cVal = A[rows][cols]
            tmp = (6 * cVal) - ((cVal - 1) * 2)
            
            if rows > 0:
                tmp -= min(cVal, A[rows-1][cols])
            if cols > 0:
                tmp -= min(cVal, A[rows][cols-1])
            if rows < len(A) - 1:
                tmp -= min(cVal, A[rows+1][cols])
            if cols < len(A[rows]) - 1:
                tmp -= min(cVal, A[rows][cols+1])

            total += tmp
            print("tmp", tmp )
        # print(total)
            # print("cVal", cVal)

    return total



a = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]

# a = [[1, 2, 1], [3, 2, 2]]

    
print(surfaceArea(a))