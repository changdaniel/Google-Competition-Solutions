from sys import stdin
n = int(input())
#convert nxn matrix to n arr

matrix = []
arr = []

for _ in range(n):
    
    matrix.append([int(i) for i in stdin.readline().split()])


if len(matrix) == 2:

    print(str(matrix[0][1] // 2) + " " + str(matrix[0][1] // 2))

elif len(matrix) == 1:

    print(matrix[0][0])

else:

    first = (matrix[0][2] - matrix[1][2] + matrix[0][1])//2
    arr.append(first)

    for n in matrix[0][1:]:

        arr.append(n-first)
    
    print(" ".join([str(a) for a in arr]))