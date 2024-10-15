def transpose_matrix(matrix):
    # Using list comprehension to transpose the matrix
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
