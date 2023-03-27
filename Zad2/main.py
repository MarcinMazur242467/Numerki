import numpy as np
import JordanSolver

def main():
    np.seterr(divide='ignore', invalid='ignore')
    size = 0
    fileName = input("Podaj nazwę pliku: ")
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for x in file:
            size += 1
        size = len(lines)
        matrix = np.zeros((size, size + 1))
        for i in range(0, size):
            row = lines[i].split(',')
            for j in range(0, size + 1):
                matrix[i, j] = row[j]
    epsilon = float(input("Podaj epsilon: "))
    solver = JordanSolver.JordanSolver(matrix,epsilon)
    print(solver.jordanGaus())


if __name__ == '__main__':
    main()
