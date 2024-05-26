def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
    
    matrices = {}
    operations = []
    matrix_name = None
    reading_matrices = True

    for line in lines:
        line = line.strip()
        if not line:
            reading_matrices = False
            continue
        
        if reading_matrices:
            if line.isalpha():
                matrix_name = line
                matrices[matrix_name] = []
            else:
                matrices[matrix_name].append(list(map(int, line.split())))
        else:
            operations.append(line)

    return matrices, operations

def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")
    
    result = [[0] * len(B[0]) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    matrices, operations = read_input('input.txt')
    
    for operation in operations:
        if '+' in operation:
            A, B = operation.split(' + ')
            result = add_matrices(matrices[A], matrices[B])
            print(f"{A} + {B}")
            print_matrix(result)
            print()
        elif '*' in operation:
            A, B = operation.split(' * ')
            result = multiply_matrices(matrices[A], matrices[B])
            print(f"{A} * {B}")
            print_matrix(result)
            print()

if __name__ == "__main__":
    main()
