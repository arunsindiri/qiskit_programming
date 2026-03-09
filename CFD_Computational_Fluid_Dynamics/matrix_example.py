import numpy as np

A = np.array([[2, 1], [1, 3]])

b = np.array([5, 6])

x = np.linalg.solve(A, b)

print("Solution:", x)
