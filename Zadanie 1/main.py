from SecantSolver import SecantSolver
from BisectionSolver import BisectionSolver
from Printer import Printer
import numpy as np


def polynominal(x):
    return x * (x * (x * (x * (5 * x + 4) - 3) + 2) + 1) - 2

def exponentialFunction(x):
    return (1 / 3) ** x - 10


def functioCnomposition(f, f1=None, f2=None):
    if f1 == None and f2 == None:
        return lambda x: f(x)
    if f1 != None and f2 == None:
        return lambda x: f(f1(x))
    return lambda x: f(f1(f2(x)))


def main():
    result = None
    function = None
    choiceStop = input("Podaj jak chcesz zatrzymac algorytm: \n1. Kryterium epsilonowe \n2. Liczba iteracji\n")
    iterations = 10
    epsilon = 0.1

    if choiceStop == "1":
        epsilon = float(input("Podaj kryterium stopu: "))
    elif choiceStop == "2":
        iterations = input("Podaj liczbe iteracji: ")

    method = input("Podaj metode wyznaczenia miejsca zerowego: \n1. Metoda bisekcji \n2. Metoda stycznych \n")
    choice = input(
        "Wybierz dostepna funkcje:\n 1.Wielomian\n2.Funkcja Trygonometryczna\n3.Funkcja Wykladnicza\n4.Zlozenie Funkcji\n"
    )
    if choice == "4":
        funcComposition = input("Podaj numery funckji ktore chcesz miec w zlozeniu [MAX 3] :(111 Wielomian(Wielomian(Wielomian(x))));11 wielomian(Wielomian(x))")
        if "2" in  funcComposition:
            user_input = input("podaj funckje trygonometryczna(1- sin;2- cos, 3-tan; 4-cot )")
            if user_input == "1":
                def trigonometricFunction(x):
                    return np.sin(x)

            elif user_input == "2":
                def trigonometricFunction(x):
                    return np.cos(x)
            elif user_input == "3":
                def trigonometricFunction(x):
                    return np.tan(x)
            elif user_input == "4":
                def trigonometricFunction(x):
                    return 1 / np.tan(x)
            else:
                raise Exception("Zly input");
    if  choice == "2":
        user_input = input("podaj funckje trygonometryczna(1- sin;2- cos, 3-tan; 4-cot )")
        if user_input == "1":
            def trigonometricFunction(x):
                return np.sin(x)

        elif user_input == "2":
            def trigonometricFunction(x):
                return np.cos(x)
        elif user_input == "3":
            def trigonometricFunction(x):
                return np.tan(x)
        elif user_input == "4":
            def trigonometricFunction(x):
                return 1 / np.tan(x)
        else:
            raise Exception("Zly input");
    while True:
        rangeLL = float(input("Podaj lewy kraniec przedzialu: \n"))
        rangeRR = float(input("Podaj prawy kraniec przedzialu: \n"))
        if rangeLL < rangeRR:
            break

    if method == "1":
        if choice == "1":
            function = polynominal
            BSolver1 = BisectionSolver(function, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = BSolver1.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = BSolver1.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "2":
            function = trigonometricFunction
            BSolver = BisectionSolver(function, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = BSolver.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = BSolver.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "3":
            function = exponentialFunction
            BSolver = BisectionSolver(function, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = BSolver.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = BSolver.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "4":
            if funcComposition == "11":
                function = functioCnomposition(polynominal, polynominal)
                BSolver = BisectionSolver(function, rangeLL, rangeRR, epsilon,
                                          iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "12":
                function = functioCnomposition(polynominal, trigonometricFunction)
                BSolver = BisectionSolver(function, rangeLL, rangeRR,
                                          epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "13":
                function = functioCnomposition(polynominal, exponentialFunction)
                BSolver = BisectionSolver(function, rangeLL, rangeRR,
                                          epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "21":
                function = functioCnomposition(trigonometricFunction, polynominal)
                BSolver = BisectionSolver(function, rangeLL, rangeRR,
                                          epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "22":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "23":
                function = functioCnomposition(trigonometricFunction, exponentialFunction)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "31":
                function = functioCnomposition(exponentialFunction, polynominal)
                BSolver = BisectionSolver(function, rangeLL, rangeRR,
                                          epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "32":
                function = functioCnomposition(exponentialFunction, trigonometricFunction)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "33":
                function = functioCnomposition(exponentialFunction, exponentialFunction)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "111":
                function = functioCnomposition(polynominal, polynominal, polynominal)
                BSolver = BisectionSolver(function, rangeLL, rangeRR,
                                          epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "112":
                function = functioCnomposition(polynominal, polynominal, trigonometricFunction)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "113":
                function = functioCnomposition(polynominal, polynominal, exponentialFunction)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "121":
                function = functioCnomposition(polynominal, trigonometricFunction, polynominal)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "122":
                function = functioCnomposition(polynominal, trigonometricFunction, trigonometricFunction)
                BSolver = BisectionSolver(
                    function, rangeLL, rangeRR,
                    epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "123":
                function = functioCnomposition(polynominal, trigonometricFunction, exponentialFunction)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "131":
                function = functioCnomposition(polynominal, exponentialFunction, polynominal)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "132":
                function = functioCnomposition(polynominal, exponentialFunction, trigonometricFunction)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "133":
                function = functioCnomposition(polynominal, exponentialFunction, exponentialFunction)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "211":
                function = functioCnomposition(trigonometricFunction, polynominal, polynominal)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "212":
                function = functioCnomposition(trigonometricFunction, polynominal, trigonometricFunction)
                BSolver = BisectionSolver(
                    function, rangeLL, rangeRR,
                    epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "213":
                function = functioCnomposition(trigonometricFunction, polynominal, exponentialFunction)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "221":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction, polynominal)
                BSolver = BisectionSolver(
                    function, rangeLL, rangeRR,
                    epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "222":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction, trigonometricFunction)
                BSolver = BisectionSolver(function
                                          , rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "223":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction, exponentialFunction)
                BSolver = BisectionSolver(function
                                          , rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "231":
                function = functioCnomposition(trigonometricFunction, exponentialFunction, polynominal)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "232":
                function = functioCnomposition(trigonometricFunction, exponentialFunction, trigonometricFunction)
                BSolver = BisectionSolver(function
                                          , rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "233":
                function = functioCnomposition(trigonometricFunction, exponentialFunction, exponentialFunction)
                BSolver = BisectionSolver(function
                                          , rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "311":
                function = functioCnomposition(exponentialFunction, polynominal, polynominal)
                BSolver = BisectionSolver(function, rangeLL,
                                          rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "312":
                function = functioCnomposition(exponentialFunction, polynominal, trigonometricFunction)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "313":
                function = functioCnomposition(exponentialFunction, polynominal, exponentialFunction)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "321":
                function = functioCnomposition(exponentialFunction, trigonometricFunction, polynominal)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "322":
                function = functioCnomposition(exponentialFunction, trigonometricFunction, trigonometricFunction)
                BSolver = BisectionSolver(
                    function, rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "323":
                function = functioCnomposition(exponentialFunction, trigonometricFunction, exponentialFunction)
                BSolver = BisectionSolver(
                    function, rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "331":
                function = functioCnomposition(exponentialFunction, exponentialFunction, polynominal)
                BSolver = BisectionSolver(function,
                                          rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "332":
                function = functioCnomposition(exponentialFunction, exponentialFunction, trigonometricFunction)
                BSolver = BisectionSolver(
                    function, rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "333":
                function = functioCnomposition(exponentialFunction, exponentialFunction, exponentialFunction)
                BSolver = BisectionSolver(
                    function, rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = BSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = BSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))

    elif method == "2":
        if choice == "1":
            function = polynominal
            SSolver = SecantSolver(function, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = SSolver.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = SSolver.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "2":
            function = trigonometricFunction
            SSolver = SecantSolver(function, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = SSolver.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = SSolver.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "3":
            function = exponentialFunction
            SSolver = SecantSolver(function, rangeLL, rangeRR, epsilon, iterations)
            if choiceStop == "1":
                result = SSolver.solveE()
                print("Miejsce zerowe funckji: " + str(result))
            elif choiceStop == "2":
                result = SSolver.solveI()
                print("Miejsce zerowe funckji: " + str(result))
        elif choice == "4":
            if funcComposition == "11":
                function = functioCnomposition(polynominal, polynominal)
                SSolver = SecantSolver(function, rangeLL, rangeRR, epsilon,
                                       iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "12":
                function = functioCnomposition(polynominal, trigonometricFunction)
                SSolver = SecantSolver(function, rangeLL, rangeRR,
                                       epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "13":
                function = functioCnomposition(polynominal, exponentialFunction)
                SSolver = SecantSolver(function, rangeLL, rangeRR,
                                       epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "21":
                function = functioCnomposition(trigonometricFunction, polynominal)
                SSolver = SecantSolver(function, rangeLL, rangeRR,
                                       epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "22":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "23":
                function = functioCnomposition(trigonometricFunction, exponentialFunction)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "31":
                function = functioCnomposition(exponentialFunction, polynominal)
                SSolver = SecantSolver(function, rangeLL, rangeRR,
                                       epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "32":
                function = functioCnomposition(exponentialFunction, trigonometricFunction)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "33":
                function = functioCnomposition(exponentialFunction, exponentialFunction)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "111":
                function = functioCnomposition(polynominal, polynominal, polynominal)
                SSolver = SecantSolver(function, rangeLL, rangeRR,
                                       epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "112":
                function = functioCnomposition(polynominal, polynominal, trigonometricFunction)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "113":
                function = functioCnomposition(polynominal, polynominal, exponentialFunction)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "121":
                function = functioCnomposition(polynominal, trigonometricFunction, polynominal)
                SSolver = SecantSolver(function, rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "122":
                function = functioCnomposition(polynominal, trigonometricFunction, trigonometricFunction)
                SSolver = SecantSolver(
                    function, rangeLL, rangeRR,
                    epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "123":
                function = functioCnomposition(polynominal, trigonometricFunction, exponentialFunction)
                SSolver = SecantSolver(functioCnomposition(polynominal, trigonometricFunction, exponentialFunction),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "131":
                function = functioCnomposition(polynominal, exponentialFunction, polynominal)
                SSolver = SecantSolver(functioCnomposition(polynominal, exponentialFunction, polynominal), rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "132":
                function = functioCnomposition(polynominal, exponentialFunction, trigonometricFunction)
                SSolver = SecantSolver(functioCnomposition(polynominal, exponentialFunction, trigonometricFunction),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "133":
                function = functioCnomposition(polynominal, exponentialFunction, exponentialFunction)
                SSolver = SecantSolver(functioCnomposition(polynominal, exponentialFunction, exponentialFunction),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "211":
                function = functioCnomposition(trigonometricFunction, polynominal, polynominal)
                SSolver = SecantSolver(functioCnomposition(trigonometricFunction, polynominal, polynominal), rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "212":
                function = functioCnomposition(trigonometricFunction, polynominal, trigonometricFunction)
                SSolver = SecantSolver(
                    functioCnomposition(trigonometricFunction, polynominal, trigonometricFunction), rangeLL, rangeRR,
                    epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "213":
                function = functioCnomposition(trigonometricFunction, polynominal, exponentialFunction)
                SSolver = SecantSolver(functioCnomposition(trigonometricFunction, polynominal, exponentialFunction),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "221":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction, polynominal)
                SSolver = SecantSolver(
                    functioCnomposition(trigonometricFunction, trigonometricFunction, polynominal), rangeLL, rangeRR,
                    epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "222":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction, trigonometricFunction)
                SSolver = SecantSolver(
                    functioCnomposition(trigonometricFunction, trigonometricFunction, trigonometricFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "223":
                function = functioCnomposition(trigonometricFunction, trigonometricFunction, exponentialFunction)
                SSolver = SecantSolver(
                    functioCnomposition(trigonometricFunction, trigonometricFunction, exponentialFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "231":
                function = functioCnomposition(trigonometricFunction, exponentialFunction, polynominal)
                SSolver = SecantSolver(functioCnomposition(trigonometricFunction, exponentialFunction, polynominal),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "232":
                function = functioCnomposition(trigonometricFunction, exponentialFunction, trigonometricFunction)
                SSolver = SecantSolver(
                    functioCnomposition(trigonometricFunction, exponentialFunction, trigonometricFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "233":
                function = functioCnomposition(trigonometricFunction, exponentialFunction, exponentialFunction)
                SSolver = SecantSolver(
                    functioCnomposition(trigonometricFunction, exponentialFunction, exponentialFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "311":
                function = functioCnomposition(exponentialFunction, polynominal, polynominal)
                SSolver = SecantSolver(functioCnomposition(exponentialFunction, polynominal, polynominal), rangeLL,
                                       rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "312":
                function = functioCnomposition(exponentialFunction, polynominal, trigonometricFunction)
                SSolver = SecantSolver(functioCnomposition(exponentialFunction, polynominal, trigonometricFunction),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "313":
                function = functioCnomposition(exponentialFunction, polynominal, exponentialFunction)
                SSolver = SecantSolver(functioCnomposition(exponentialFunction, polynominal, exponentialFunction),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "321":
                function = functioCnomposition(exponentialFunction, trigonometricFunction, polynominal)
                SSolver = SecantSolver(functioCnomposition(exponentialFunction, trigonometricFunction, polynominal),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "322":
                function = functioCnomposition(exponentialFunction, trigonometricFunction, trigonometricFunction)
                SSolver = SecantSolver(
                    functioCnomposition(exponentialFunction, trigonometricFunction, trigonometricFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "323":
                function = functioCnomposition(exponentialFunction, trigonometricFunction, exponentialFunction)
                SSolver = SecantSolver(
                    functioCnomposition(exponentialFunction, trigonometricFunction, exponentialFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "331":
                function = functioCnomposition(exponentialFunction, exponentialFunction, polynominal)
                SSolver = SecantSolver(functioCnomposition(exponentialFunction, exponentialFunction, polynominal),
                                       rangeLL, rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "332":
                function = functioCnomposition(exponentialFunction, exponentialFunction, trigonometricFunction)
                SSolver = SecantSolver(
                    functioCnomposition(exponentialFunction, exponentialFunction, trigonometricFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
            elif funcComposition == "333":
                function = functioCnomposition(exponentialFunction, exponentialFunction, exponentialFunction)
                SSolver = SecantSolver(
                    functioCnomposition(exponentialFunction, exponentialFunction, exponentialFunction), rangeLL,
                    rangeRR, epsilon, iterations)
                if choiceStop == "1":
                    result = SSolver.solveE()
                    print("Miejsce zerowe funckji: " + str(result))
                elif choiceStop == "2":
                    result = SSolver.solveI()
                    print("Miejsce zerowe funckji: " + str(result))
    Pprinter = Printer(result, function, rangeLL, rangeRR)
    Pprinter.printPlot()


if __name__ == '__main__':
    main()
