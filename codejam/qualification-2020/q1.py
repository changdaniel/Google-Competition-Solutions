from sys import stdin
T = int(input())

def read_matrix():
    N = int(input())
    rows = []
    for i in range(N):
        rows.append([int(x) for x in stdin.readline().split(" ")])

    return rows

def read_matrices(T):
    
    matrices = []
    for i in range(T):
        matrices.append(read_matrix())
    
    return matrices
    
def calc_trace(matrix):

    total = 0
    for i in range(len(matrix)):

        total += matrix[i][i]
    
    return total

def calc_repeats(matrix):
    valid = set([i for i in range(1, len(matrix) + 1)])
    row_total = 0 
    for row in matrix:
        row_total += 1 if len(set(row) & valid) != len(matrix) else 0
    
    col_total = 0
    transposed_matrix = [list(i) for i in zip(*matrix)]
    for col in transposed_matrix:
        col_total += 1 if len(set(col) & valid) != len(matrix) else 0

    return row_total, col_total


matrices = read_matrices(T)
out = ""
for matrix in matrices:

    out += "{} {} {}\n".format(calc_trace(matrix),*calc_repeats(matrix))

print(out[:-1])