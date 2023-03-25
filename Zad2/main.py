import numpy as np

def jordanGaus(matrix,epsilon):
    size = len(matrix)
    vector = np.zeros(size)
    squareMatrix = matrix[:, :-1]
    # for i in range(0,len(matrix)):
    #     vector[i] = matrix[len(matrix)-1][i]
    if abs(np.linalg.det(squareMatrix)-0.0) < epsilon:
        return "Nieoznaczony lub sprzeczny"




    print(matrix)
    print(vector)
    for i in range(0,size-2):
        if abs(matrix[i, i] - 0.0) < epsilon:
            return "FAILURE"
        for j in range(i+1,size-1):
            m = -(matrix[j,i]/matrix[i,i])
            for k in range(i+1,size):
                matrix[j,k] = matrix[j,k]+m*matrix[i,k]
    for i in range(size-1,0,-1):
        if abs(matrix[i,i] - 0.0) < epsilon:
            return "FAILURE"
        suma = matrix[i,size]
        for j in range(size-1,i+1):
            suma = suma - matrix[i,j]*vector[j]
        vector[i] =-(suma/matrix[i,i])
    return vector

def main():
    size = 0
    with open("matrix.txt",'r') as file:
        lines = file.readlines()
        for x in file:
            size+=1
        size = len(lines)
        matrix = np.zeros((size, size+1))
        for i in range(0,size):
            row = lines[i].split(',')
            for j in range(0,size+1):
                matrix[i,j] = row[j]
    print(jordanGaus(matrix,0.00001))

if __name__ == '__main__':
    main();