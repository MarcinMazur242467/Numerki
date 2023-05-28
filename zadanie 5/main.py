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
nodes=0


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

        self.label = tk.Label(self.root, text="Wprowadź ilosc wezlow podczas calkowania", font=('Arial', 18))
        self.label.pack(pady=10)
        self.text4 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text4.pack()
        self.button5 = tk.Button(self.root, text="Wprowadz wezly", command=self.getNodes)
        self.button5.pack()


        self.button_authors = tk.Button(self.root, text="Autorzy", command=self.openPopup)
        self.button_authors.place(relx=0.95, rely=0.95, anchor="se")

        self.label = tk.Label(self.root, text="Aproksymacja: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text5 = tk.Text(self.root, height=2, font=('Arial', 12))
        self.text5.config(state="disabled")
        self.text5.pack()

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

    def getNodes(self):
        global nodes
        user_input = self.text4.get("1.0",tk.END)
        nodes = int(user_input)
        return nodes

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

    def plot_approximation(self,a, b, N):
        x = np.linspace(a, b, 100)  # x values for evaluation
        y = self.calculateFunction(x)  # Original function values

        approximation = [self.aproximation(i, N) for i in x]

        plt.plot(x, y, label='Funkcja')
        plt.plot(x, approximation, label='Aproksymacja')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Aproksymacja Wielomianami Chebycheva')
        plt.show()

    def integrate_gauss(self, f,n):
        result = 0
        weight = math.pi / n
        for i in range(1, n+1):
            node = math.cos(((2 * i - 1) * math.pi) / (2 * n))
            result += (f(node))/(1/(math.sqrt(1-(node*node))))
        return weight * result

    def coefficient(self,k):
        result = self.integrate_gauss(lambda t: self.calculateFunction(t) * Tk(k, t) * (1 / np.sqrt(1 - t * t)),nodes)
        return result * (2 / np.pi)



    def aproximation(self,x, N):
        sum = 0
        for i in range(1, N + 1):
            sum += self.coefficient(i) * Tk(i, x)
        return self.coefficient(0) / 2 * Tk(0, x) + sum

def Tk(n, x):
    return scipy.special.eval_chebyt(n,x)

GUI()