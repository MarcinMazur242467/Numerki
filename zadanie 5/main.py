import math
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

integralRange = [0, 0]
approximationRange = [0, 0]
degree = 0
function = None
epsilon = 0.001


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zadanie 5")
        self.root.minsize(1000, 750)

        self.label = tk.Label(self.root, text="Wprowadź wzór funkcji: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root, height=2)
        self.frame.pack()

        self.text = tk.Text(self.frame, height=2, font=('Arial', 12))
        self.text.pack(side=tk.LEFT, expand=True)

        self.button = tk.Button(self.root, text="Wprowadz funkcje", command=self.getFunction)
        self.button.pack()

        self.label = tk.Label(self.root, text="Wprowadź przedział aproksymacji: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text2 = tk.Text(self.root, height=1, font=('Arial', 12))
        self.text2.pack()

        self.button3 = tk.Button(self.root, text="Wprowadź przedział", command=self.getApproximationRange)
        self.button3.pack()

        self.label = tk.Label(self.root, text="Wprowadź stopień wielomianu aproksymującego: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text6 = tk.Text(self.root, height=1, font=('Arial', 12))
        self.text6.pack()

        self.button7 = tk.Button(self.root, text="Wprowadź stopień", command=self.getDegree)
        self.button7.pack()

        self.label = tk.Label(self.root, text="Wprowadź przedział całkowania dla wzoru Simpsona: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text3 = tk.Text(self.root, height=1, font=('Arial', 12))
        self.text3.pack()

        self.button4 = tk.Button(self.root, text="Wprowadź przedział", command=self.getRange)
        self.button4.pack()

        self.label = tk.Label(self.root, text="Kwadratura Newtona-Cotesa: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text4 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text4.config(state="disabled")
        self.text4.pack()

        self.button5 = tk.Button(self.root, text="Oblicz całke", command=self.simpsonMethod)
        self.button5.pack()

        self.button_authors = tk.Button(self.root, text="Autorzy", command=self.openPopup)
        self.button_authors.place(relx=0.95, rely=0.95, anchor="se")

        self.label = tk.Label(self.root, text="Aproksymacja: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text5 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text5.config(state="disabled")
        self.text5.pack()

        # self.button6 = tk.Button(self.root, text="Oblicz błąd aproksymacji", command=self.approximationError)
        # self.button6.pack()

        self.button2 = tk.Button(self.root, text="Wygeneruj wykres", command=self.printPlot)
        self.button2.pack()

        self.root.mainloop()

    def getFunction(self):
        global function
        function = self.text.get("1.0", tk.END)

    def calculateFunction(self, x):
        return eval(function)

    def getRange(self):
        global integralRange
        user_input = self.text3.get("1.0", tk.END)
        numbers_as_strings = user_input.split(",")
        integralRange = [float(number.strip()) for number in numbers_as_strings]

    def getApproximationRange(self):
        global approximationRange
        user_input = self.text2.get("1.0", tk.END)
        numbers_as_strings = user_input.split(",")
        approximationRange = [float(number.strip()) for number in numbers_as_strings]

    def printPlot(self):
        x1 = np.linspace(-1, 1, 1000)
        y1 = self.calculateFunction(x1)
        x2, approx_f, error = self.chebyshev_approximation(approximationRange[0], approximationRange[1], degree)
        y2 = []
        for i in x2:
            y2.append(self.calculateFunction(i))
        plt.plot(x1, y1, label='original function')
        plt.plot(x2, y2, label='approximation function')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.show()

    def getDegree(self):
        global degree
        user_input = self.text6.get("1.0", tk.END)
        degreeAsString = user_input
        degree = int(degreeAsString)
        return degree

    # def getEpsilon(self):
    #     global epsilon
    #     user_input = self.text6.get("1.0", tk.END)
    #     epsilonAsString = user_input
    #     epsilon = float(epsilonAsString)
    #     return epsilon

    def openPopup(self):
        popup = tk.Toplevel(self.root, )
        popup.title("Autorzy")
        popup.geometry("400x200")
        label = tk.Label(popup, text="Piotr Płeska 242499")
        label.pack(padx=20, pady=20)
        label = tk.Label(popup, text="Marcin Mazur 242467")
        label.pack(padx=20, pady=20)
        button = tk.Button(popup, text="Wyjdź", command=popup.destroy)
        button.pack(pady=10)

    def simpsonMethod(self):
        n = 3
        result = 1
        s = 0
        a = 0
        while math.fabs(result - s) > epsilon:
            a += 1
            result = s
            st = 0
            dx = (integralRange[1] - integralRange[0]) / n

            for i in range(1, n + 1):
                x = integralRange[0] + i * dx
                st += self.calculateFunction(x - dx / 2)
                if i < n:
                    s += self.calculateFunction(x)

            s = dx / 6 * (self.calculateFunction(integralRange[0]) + self.calculateFunction(
                integralRange[1]) + 2 * s + 4 * st)
            n = n * 2
        print(a)
        self.text4.config(state="normal")
        self.text4.delete('1.0', 'end')
        self.text4.insert(tk.END, str(s))
        self.text4.config(state="disabled")
        return s

    def chebyshev_approximation(self, a, b, deg):
        # Oblicz współczynniki wielomianów Czebyszewa
        def chebyshev_coeffs(n):
            def integrand(x, k):
                return self.calculateFunction(x) * np.cos(k * np.arccos((2 * x - a - b) / (b - a)))

            coeffs = []
            for i in range(n + 1):
                coeff, _ = quad(integrand, a, b, args=(i,))
                coeff *= 2 / (b - a)
                coeffs.append(coeff)

            return coeffs

        # Oblicz wartość wielomianu Czebyszewa o stopniu n
        def chebyshev_polynomial(x, coeffs):
            p0, p1 = 1, x
            value = p0 * coeffs[0]

            for i in range(1, len(coeffs)):
                p2 = 2 * x * p1 - p0
                value += p2 * coeffs[i]
                p0, p1 = p1, p2

            return value

        # Oblicz błąd normy L2
        def l2_error(approx_f):
            def squared_error(x):
                return (self.calculateFunction(x) - approx_f(x)) ** 2

            error, _ = quad(squared_error, a, b)
            return np.sqrt(error)

        # Oblicz współczynniki wielomianu aproksymującego
        coeffs = chebyshev_coeffs(deg)

        # Utwórz funkcję aproksymującą
        def approx_f(x):
            return chebyshev_polynomial((2 * x - a - b) / (b - a), coeffs)

        # Oblicz błąd normy L2 aproksymacji
        error = l2_error(approx_f)

        return coeffs, approx_f, error


GUI()
