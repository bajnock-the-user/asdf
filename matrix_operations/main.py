def read_matrices(file):
    matrices = {}
    lines = file.read().splitlines()
    i = 0
    while i < len(lines):
        if lines[i]:
            matrix_name = lines[i]
            i += 1
            matrix = []
            while i < len(lines) and lines[i]:
                matrix.append(list(map(int, lines[i].split())))
                i += 1
            matrices[matrix_name] = matrix
        i += 1
    return matrices

def add_matrices(A, B):
    rows, cols = len(A), len(A[0])
    return [[A[r][c] + B[r][c] for c in range(cols)] for r in range(rows)]

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def main():
    # Read matrices from input.txt
    with open('./input.txt', 'r') as file:
        matrices = read_matrices(file)
    
    # Read operations
    with open('matrix_operations/operations.txt', 'r') as file:
        operations = file.read().splitlines()
    
    for operation in operations:
        A, op, B = operation.split()
        if op == '+':
            result = add_matrices(matrices[A], matrices[B])
        elif op == '*':
            result = multiply_matrices(matrices[A], matrices[B])
        
        print(f"{A} {op} {B}")
        for row in result:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
