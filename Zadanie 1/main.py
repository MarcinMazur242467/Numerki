from SecantSolver import SecantSolver
from BisectionSolver import BisectionSolver

import math


def linearFunction(x):
    return x - 1


def polynominal(x):
    return 5 * x * x * x * x * x + 4 * x * x * x * x - 3 * x * x * x + 2 * x * x + x - 10


def trigonometricFunction(x):
    return math.sin(x) * math.sin(x) * math.cos(x)


def exponentialFunction(x):
    return (1 / 3) ** x - 10


def functioCnomposition(f, x, f1=None, f2=None):
    if f1 == None and f2 == None:
        return f(x)
    if f1 != None:
        return f(f1(x))
    return f(f1(f2(x)))


def main():
    print(functioCnomposition(linearFunction, 10, linearFunction))

    # BSolver = BisectionSolver(functioCnomposition, -1, 1, 0.00001,500)
    # print(BSolver.solveE())
    # print(BSolver.solveI())
    #
    # SSolver = SecantSolver(functioCnomposition, -10, 10, 0.00001,20)
    # print(SSolver.solveE())
    # print(SSolver.solveI())
    root = None

    # użytkownik ma wybrać jakie złożenia
    choiceStop = input("Podaj jak chcesz zatrzymac algorytm: \n1. Kryterium epsilonowe \n2. Liczba iteracji\n")
    iterations = 10
    epsilon = 0.1

    if choiceStop == "1":
        epsilon = float(input("Podaj kryterium stopu: "))
    elif choiceStop == "2":
        iterations = input("Podaj liczbe iteracji: ")

    method = input("Podaj metode wyznaczenia miejsca zerowego: \n1. Metoda bisekcji \n2. Metoda stycznych \n")
    choice = input(
        """Wybierz dostepna funkcje:
        1. Wielomian
        2. Funkcja Trygonometryczna
        3. Funkcja Wykladnicza
        4. Zlozenie Funkcji\n"""
    )

    funcComposition = input("""
        Podaj numery funckji ktore chcesz miec w zlozeniu [MAX 3] :(111 Wielomian(Wielomian(Wielomian(x))));11 wielomian(Wielomian(x))
        """)
    while True:
        rangeLL = int(input("Podaj lewy kraniec przedzialu: \n"))
        rangeRR = int(input("Podaj prawy kraniec przedzialu: \n"))
        if rangeLL < rangeRR:
            break

    if method == "1":
        if choice == "1":
            BSolver1 = BisectionSolver(polynominal, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = BSolver1.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = BSolver1.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "2":
            BSolver = BisectionSolver(trigonometricFunction, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                print("Miejsce zerowe funckji: " + str(BSolver.solveE()))
            elif choiceStop == "2":
                print("Miejsce zerowe funckji: " + str(BSolver.solveI()))
        elif choice == "3":
            BSolver = BisectionSolver(exponentialFunction, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                print("Miejsce zerowe funckji: " + str(BSolver.solveE()))
            elif choiceStop == "2":
                print("Miejsce zerowe funckji: " + str(BSolver.solveI()))
        elif choice == "4":
            if funcComposition == "11":
                print()
            elif funcComposition == "12":

            elif funcComposition == "13":

            elif funcComposition == "21":

            elif funcComposition == "22":

            elif funcComposition == "23":

            elif funcComposition == "31":

            elif funcComposition == "32":

            elif funcComposition == "33":

            elif funcComposition == "111":

            elif funcComposition == "112":

            elif funcComposition == "113":

            elif funcComposition == "121":

            elif funcComposition == "122":

            elif funcComposition == "123":

            elif funcComposition == "131":

            elif funcComposition == "132":

            elif funcComposition == "133":

            elif funcComposition == "211":

            elif funcComposition == "212":

            elif funcComposition == "213":

            elif funcComposition == "221":

            elif funcComposition == "222":

            elif funcComposition == "223":

            elif funcComposition == "231":

            elif funcComposition == "232":

            elif funcComposition == "233":

            elif funcComposition == "311":

            elif funcComposition == "312":

            elif funcComposition == "313":

            elif funcComposition == "321":

            elif funcComposition == "322":

            elif funcComposition == "323":

            elif funcComposition == "331":

            elif funcComposition == "332":

            elif funcComposition == "333":

    elif method == "2":
        if choice == "1":
            pass
        elif choice == "2":
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            if funcComposition == "11":
                print();
            elif funcComposition == "12":
            elif funcComposition == "13":
            elif funcComposition == "21":
            elif funcComposition == "22":
            elif funcComposition == "23":
            elif funcComposition == "31":
            elif funcComposition == "32":
            elif funcComposition == "33":
            elif funcComposition == "111":
            elif funcComposition == "112":
            elif funcComposition == "113":
            elif funcComposition == "121":
            elif funcComposition == "122":
            elif funcComposition == "123":
            elif funcComposition == "131":
            elif funcComposition == "132":
            elif funcComposition == "133":
            elif funcComposition == "211":
            elif funcComposition == "212":
            elif funcComposition == "213":
            elif funcComposition == "221":
            elif funcComposition == "222":
            elif funcComposition == "223":
            elif funcComposition == "231":
            elif funcComposition == "232":
            elif funcComposition == "233":
            elif funcComposition == "311":
            elif funcComposition == "312":
            elif funcComposition == "313":
            elif funcComposition == "321":
            elif funcComposition == "322":
            elif funcComposition == "323":
            elif funcComposition == "331":
            elif funcComposition == "332":
            elif funcComposition == "333":


if __name__ == '__main__':
    main()
