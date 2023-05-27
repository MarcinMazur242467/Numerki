import math
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import scipy

integralRange = [0, 0]
approximationRange = [0, 0]
degree = 0
function = None
epsilon = 0.01


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

        # self.label = tk.Label(self.root, text="Kwadratura Newtona-Cotesa: ", font=('Arial', 18))
        # self.label.pack(pady=10)

        # self.text4 = tk.Text(self.root, height=2, font=('Arial', 12))
        # self.text4.config(state="disabled")
        # self.text4.pack()

        # self.button5 = tk.Button(self.root, text="Oblicz całke", command=self.simpsonMethod)
        # self.button5.pack()

        self.button_authors = tk.Button(self.root, text="Autorzy", command=self.openPopup)
        self.button_authors.place(relx=0.95, rely=0.95, anchor="se")

        self.label = tk.Label(self.root, text="Aproksymacja: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text5 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text5.config(state="disabled")
        self.text5.pack()

        # self.button6 = tk.Button(self.root, text="Oblicz błąd aproksymacji", command=self.approximationError)
        # self.button6.pack()

        self.button2 = tk.Button(self.root, text="Wygeneruj wykres", command=lambda:self.plot_approximation(approximationRange[0],approximationRange[1],degree))
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

    def dupa(self,x):
        return x*x
    def openPopup(self):
        print((2/np.pi)*self.integrate_simpson(lambda t:self.dupa(t) * Tk(2, t) * (1 / np.sqrt(1 - t * t)),-1,1))
        print(self.integrate_simpson(lambda t: self.dupa(t),-1,1))
        popup = tk.Toplevel(self.root, )
        popup.title("Autorzy")
        popup.geometry("400x200")
        label = tk.Label(popup, text="Piotr Płeska 242499")
        label.pack(padx=20, pady=20)
        label = tk.Label(popup, text="Marcin Mazur 242467")
        label.pack(padx=20, pady=20)
        button = tk.Button(popup, text="Wyjdź", command=popup.destroy)
        button.pack(pady=10)

    def plot_approximation(self,a, b, N):
        x = np.linspace(a, b, 100)  # x values for evaluation
        y = self.calculateFunction(x)  # Original function values

        approximation = [self.aproximation(i, N) for i in x]

        plt.plot(x, y, label='Original Function')
        plt.plot(x, approximation, label='Approximation')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Chebyshev Polynomial Approximation')
        plt.show()

    # def simpsonMethod(self,function):
    #     n = 1000000
    #
    #     # Calculate the step size
    #     h = 2 / n
    #
    #     # Initialize the sum variables
    #     sum_odd = 0
    #     sum_even = 0
    #
    #     # Perform the summation for odd and even terms
    #     for i in range(1, n, 2):
    #         sum_odd += function(-1 + i * h)
    #
    #     for i in range(2, n, 2):
    #         sum_even += function(-1 + i * h)
    #
    #     # Calculate the integral value using Simpson's rule
    #     integral_value = (h / 3) * (function(-0.9999999999999999) + 4 * sum_odd + 2 * sum_even + function(0.9999999999999999))
    #
    #     return integral_value

    # def simpsonMethod(self,function):
    #     n = 100
    #     print(function(-1))
    #     result = 1
    #     s = 0
    #     a = 0
    #     # while n > 200:
    #     while math.fabs(result - s) > 0.00001:
    #         a += 1
    #         result = s
    #         st = 0
    #         dx = (integralRange[1] - integralRange[0]) / n
    #
    #         for i in range(1, n + 1):
    #             x = integralRange[0] + i * dx
    #             st += function(x - dx / 2)
    #             if i < n:
    #                 s += function(x)
    #         s = dx / 6 * (function(function(-0.9999999999999999)) + function(function(-0.9999999999999999)) + 2 * s + 4 * st)
    #         # s = dx / 6 * (function(integralRange[0]) + function(integralRange[1]) + 2 * s + 4 * st)
    #         n = n * 2
    #     return s

    def integrate_simpson(self, f, a, b, n=1000):
        """
        Calculate the definite integral of a function using Simpson's rule.

        Arguments:
        f -- The function to be integrated.
        a -- The lower limit of integration.
        b -- The upper limit of integration.
        n -- The number of subintervals to use (default: 1000).

        Returns:
        The value of the definite integral.
        """
        if a == b:
            return 0  # Range is zero, so integral is zero

        if n % 2 != 0:
            n += 1  # Ensure even number of subintervals

        h = (b - a) / n  # Width of each subinterval
        integral = f(a) + f(b)  # Start with endpoints of the range

        for i in range(1, n):
            x = a + i * h  # Calculate the x-coordinate of the current subinterval

            try:
                if i % 2 == 0:
                    integral += 2 * f(x)  # Even subinterval
                else:
                    integral += 4 * f(x)  # Odd subinterval
            except ZeroDivisionError:
                continue  # Skip division by zero errors

        integral *= h / 3

        return integral

    def coefficient(self,k):
        # result, _ = scipy.integrate.quad(lambda t: self.calculateFunction(t) * Tk(k, t) * (1 / np.sqrt(1 - t * t)), -1, 1)
        result = self.integrate_simpson(lambda t:self.calculateFunction(t) * Tk(2, t) * (1 / np.sqrt(1 - t * t)),integralRange[0],integralRange[1])
        print(result)
        return result * (2 / np.pi)



    def aproximation(self,x, N):
        sum = 0
        for i in range(1, N + 1):
            sum += self.coefficient(i) * Tk(i, x)
        return self.coefficient(0) / 2 * Tk(0, x) + sum

def Tk(n, x):
    return scipy.special.eval_chebyt(n,x)

GUI()