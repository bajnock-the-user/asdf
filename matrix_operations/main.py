def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    matrices = {}
    operations = []
    current_matrix = None

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.isalpha() and line not in matrices:
            current_matrix = line
            matrices[current_matrix] = []
        elif current_matrix is not None:
            matrices[current_matrix].append(list(map(int, line.split())))
        elif line.startswith('operations'):
            break
        else:
            operations.append(line)
    
    # Reading the operations
    operations_start = False
    for line in lines:
        line = line.strip()
        if line.startswith('operations'):
            operations_start = True
            continue
        if operations_start and line:
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

def evaluate_expression(expression, matrices):
    elements = expression.split()
    result = matrices[elements[0]]
    
    i = 1
    while i < len(elements):
        operator = elements[i]
        next_matrix = matrices[elements[i + 1]]
        
        if operator == '+':
            result = add_matrices(result, next_matrix)
        elif operator == '*':
            result = multiply_matrices(result, next_matrix)
        
        i += 2
    
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    matrices, operations = read_input('input.txt')
    
    for operation in operations:
        result = evaluate_expression(operation, matrices)
        print(f"{operation}")
        print_matrix(result)
        print()

if __name__ == "__main__":
    main()
