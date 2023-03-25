import math
import numpy as np


def jordanGaus(matrix, epsilon):
    size = len(matrix)
    vector = np.zeros(size)
    squareMatrix = matrix[:, :-1]
    # if abs(np.linalg.det(squareMatrix) - 0.0) < epsilon:
    #     return "Nieoznaczony lub sprzeczny"
    # Sprowadzamy do postaci schodkowej dolnej
    for i in range(0, size - 1):
        if abs(matrix[i, i] - 0.0) < epsilon:
            # Dodajemy do siebie wiersze, zeby uniknac zer w dzielniku
            for z in range(0, size + 1):
                if i == size:
                    matrix[i][z] += matrix[0][z]
                else:
                    matrix[i][z] += matrix[i + 1][z]
        # Sprawdzamy czy po dodaniu do siebie wierszy nie ma zadnych nanow (wtedy nieoznaczony)
        for j in range(0, size):
            for k in range(0, size + 1):
                if math.isnan(matrix[i][j]):
                    return "Układ równań jest nieoznaczony!"
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
        # Sprawdzamy czy po dodaniu do siebie wierszy nie ma zadnych nanow (wtedy nieoznaczony)
        for j in range(0, size):
            for k in range(0, size + 1):
                if math.isnan(matrix[i][j]):
                    return "Układ równań jest nieoznaczony!"
        for j in range(i - 1, -1, -1):
            m = -(matrix[j, i] / matrix[i, i])
            for k in range(size, i - 1, -1):
                matrix[j, k] += m * matrix[i, k]
    # Sprawdzamy wyznacznik
    if abs(np.linalg.det(squareMatrix) - 0.0) < epsilon:
        return "Układ równan jest sprzeczny!"
    for i in range(0, size):
        if matrix[i][i] == 0:
            vector[i] = 0
        else:
            vector[i] = matrix[i, size] / matrix[i][i]
    return vector


def main():
    np.seterr(divide='ignore', invalid='ignore')
    size = 0
    with open("matrix.txt", 'r') as file:
        lines = file.readlines()
        for x in file:
            size += 1
        size = len(lines)
        matrix = np.zeros((size, size + 1))
        for i in range(0, size):
            row = lines[i].split(',')
            for j in range(0, size + 1):
                matrix[i, j] = row[j]
    print(jordanGaus(matrix, 0.000000001))


if __name__ == '__main__':
    main()
