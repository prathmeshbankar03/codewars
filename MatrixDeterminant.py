import numpy as np
def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    else:
        result = np.linalg.det(matrix)
        return round(result)