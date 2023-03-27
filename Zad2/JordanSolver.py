import numpy as np
class JordanSolver:
    def __init__(self,matrix,epsilon):
        self.matrix = matrix
        self.epsilon = epsilon

    def jordanGaus(self):
        matrix = self.matrix
        epsilon = self.epsilon
        size = len(matrix)
        vector = np.zeros(size)
        squareMatrix = matrix[:, :-1]
        # Sprowadzamy do postaci schodkowej dolnej
        for i in range(0, size - 1):
            if abs(matrix[i, i] - 0.0) < epsilon:
                # Dodajemy do siebie wiersze, zeby uniknac zer w dzielniku
                for z in range(0, size + 1):
                    if i == size:
                        matrix[i][z] += matrix[0][z]
                    else:
                        matrix[i][z] += matrix[i + 1][z]
            for j in range(i + 1, size):
                m = -(matrix[j, i] / matrix[i, i])
                for k in range(i, size + 1):
                    matrix[j, k] += m * matrix[i, k]
        # Sprowadzamy do macierzy jednostkowej
        for i in range(size - 1, 0, -1):
            if abs(matrix[i, i] - 0.0) < epsilon:
                # Dodajemy do siebie wiersze, zeby uniknac zer w dzielniku
                for z in range(size - 1, 0):
                    if i == size - 1:
                        matrix[i][z] += matrix[0][z]
                    else:
                        matrix[i][z] += matrix[i + 1][z]
            for j in range(i - 1, -1, -1):
                m = -(matrix[j, i] / matrix[i, i])
                for k in range(size, i - 1, -1):
                    matrix[j, k] += m * matrix[i, k]
        for j in range(matrix.shape[0]):
            if abs(matrix[j][j] - 0.0) < epsilon:
                if abs(matrix[j][j + 1] - 0.0) < epsilon:
                    return "Układ jest nieoznaczony"
                else:
                    return "Układ jest sprzeczny"
        # Sprawdzamy wyznacznik
        if abs(np.linalg.det(squareMatrix) - 0.0) < epsilon:
            return "Układ jest nieoznaczony!"
        for i in range(0, size):
            if matrix[i][i] == 0:
                vector[i] = 0
            else:
                vector[i] = matrix[i, size] / matrix[i][i]
        return vector