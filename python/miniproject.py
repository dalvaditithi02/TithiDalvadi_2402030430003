import numpy as np

# 1. Create two random matrices (3x3)
matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

# 2. Matrix multiplication
matrix_multiply = np.dot(matrix_a, matrix_b)

# 3. Matrix transpose
matrix_transpose = np.transpose(matrix_a)

# 4. Flattening a matrix (converting it into a 1D array)
flattened_matrix = matrix_a.flatten()

# 5. Calculate mean, median, and standard deviation of a matrix
mean_val = np.mean(matrix_a)
median_val = np.median(matrix_a)
std_dev_val = np.std(matrix_a)

# Print the results
print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("\nMatrix A * Matrix B (Multiplication):")
print(matrix_multiply)
print("\nTranspose of Matrix A:")
print(matrix_transpose)
print("\nFlattened Matrix A:")
print(flattened_matrix)
print("\nMean of Matrix A:", mean_val)
print("Median of Matrix A:", median_val)
print("Standard Deviation of Matrix A:", std_dev_val)
