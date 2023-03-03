from SecantSolver import SecantSolver
from BisectionSolver import BisectionSolver


import math

def linearFunction(x):
    return x-1

def polynominal(x):
    return 4 * x * x * x * x - 3 * x * x * x + 2 * x * x + x - 10


def trigonometricFunction(x):
    return math.sin(x) * math.sin(x) * math.cos(x)


def exponentialFunction(x):
    return (1/3)**x - 10


def functioCnomposition(x):
    return polynominal(linearFunction(x))





def main():
    # BSolver = BisectionSolver(functioCnomposition, -1, 1, 0.00001,500)
    # print(BSolver.solveE())
    # print(BSolver.solveI())
    #
    # SSolver = SecantSolver(functioCnomposition, -10, 10, 0.00001,20)
    # print(SSolver.solveE())
    # print(SSolver.solveI())

    choiceStop = input("Podaj jak chcesz zatrzymac algorytm: \n1. Kryterium epsilonowe \n2. Liczba iteracji\n")
    iterations = 10
    epsilon = 0.1
    if choiceStop == "1":
        epsilon = float(input("Podaj kryterium stopu: "))
    elif choiceStop == "2":
        iterations = input("Podaj liczbe iteracji: ")

    method = input("Podaj metode wyznaczenia miejsca zerowego: \n1. Metoda bisekcji \n2. Metoda stycznych \n")
    choice = input("""Wybierz dostepna funkcje:
1. Wielomian
2. Funkcja Trygonometryczna
3. Funkcja Wykladnicza
4. Zlozenie Funkcji\n""")


    while True:
        rangeLL = int(input("Podaj lewy kraniec przedzialu: \n"))
        rangeRR = int(input("Podaj prawy kraniec przedzialu: \n"))
        print(rangeLL)
        print(rangeRR)
        if rangeLL <rangeRR:
            break

    if method == "1":
        if choice == "1":
            BSolver = BisectionSolver(polynominal, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                print("Miejsce zerowe funckji: " + BSolver.solveE())
            elif choiceStop == "2":
                print("Miejsce zerowe funckji: " + BSolver.solveI())
        elif choice == "2":
            BSolver = BisectionSolver(trigonometricFunction, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                print("Miejsce zerowe funckji: " + BSolver.solveE())
            elif choiceStop == "2":
                print("Miejsce zerowe funckji: " + BSolver.solveI())
        elif choice == "3":
            BSolver = BisectionSolver(exponentialFunction, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                print("Miejsce zerowe funckji: " + BSolver.solveE())
            elif choiceStop == "2":
                print("Miejsce zerowe funckji: " + BSolver.solveI())
        elif choice == "4":
            BSolver = BisectionSolver(functioCnomposition, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                print("Miejsce zerowe funckji: " + BSolver.solveE())
            elif choiceStop == "2":
                print("Miejsce zerowe funckji: " + BSolver.solveI())
    elif method == "2":
        if choice == "1":
            print("dupa1")
        elif choice == "2":
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            print()


if __name__ == '__main__':
    main()
