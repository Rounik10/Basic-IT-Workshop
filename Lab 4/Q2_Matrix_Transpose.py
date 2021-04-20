def printMat(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j],end = ' ')
        print()

M = [[1,2],[4,5],[3,6]]
T = [[0,0,0],[0,0,0]]
for i in range(len(M)):
    for j in range(len(M[0])):
        T[j][i]=M[i][j]
print("Matrix M:")
printMat(M)
print('M transpose:')
printMat(T)