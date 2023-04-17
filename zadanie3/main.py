import tkinter as tk
import sympy
import matplotlib.pyplot as plt
import numpy as np


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zadanie 3")
        self.root.minsize(1000, 600)

        self.label = tk.Label(self.root, text="Wprowadź wzór funkcji: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root, height=2)
        self.frame.pack()

        self.text = tk.Text(self.frame, height=2, font=('Arial', 12))
        self.text.pack(side=tk.LEFT, expand=True)

        self.button = tk.Button(self.root, text="Wprowadz funkcje", command=self.getFunction)
        self.button.pack()

        self.button2 = tk.Button(self.root, text="Wygeneruj wykres", command=self.printOriginalFunctionPlot)
        self.button2.pack()

        self.label = tk.Label(self.root, text="Wprowadz położenia węzłow interpolacyjnych: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text2 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text2.pack()

        self.button2 = tk.Button(self.root, text="Wprowadz położenia węzłow interpolacyjnych", command=self.getFunctionPoints)
        self.button2.pack()

        self.label = tk.Label(self.root, text="Wprowadź przedział interpolacji (po przecinku): ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text3 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text3.pack()

        self.button3 = tk.Button(self.root, text="Wprowadź przedział interpolacji", command=self.getInterpolationRange)
        self.button3.pack()

        self.label = tk.Label(self.root, text="Wzór interpolacji: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.root.mainloop()

    def getFunction(self):
        user_input = self.text.get("1.0", tk.END)
        # wartosc bezwzgledna wpisywac jako "Abs(x)"
        expr = sympy.parse_expr(user_input)
        f = sympy.lambdify('x', expr, 'numpy')
        print(f)
        return f

    def printOriginalFunctionPlot(self):
        f = self.getFunction()
        x = np.linspace(-10, 10, 1000)
        # Wartosci funkcji
        y = f(x)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.plot(x, y)
        ax.grid()
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)
        plt.show()

    def getFunctionPoints(self):
        user_input = self.text2.get("1.0", tk.END)
        numbers_as_strings = user_input.split(",")
        numbers_as_float = [float(number.strip()) for number in numbers_as_strings]
        print(numbers_as_float)
        return numbers_as_float

    def getInterpolationRange(self):
        user_input = self.text3.get("1.0", tk.END)
        numbers_as_strings = user_input.split(",")
        numbers_as_float = [float(number.strip()) for number in numbers_as_strings]
        print(numbers_as_float)
        return numbers_as_float


GUI()

