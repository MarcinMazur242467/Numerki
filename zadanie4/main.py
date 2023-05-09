import math
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

integralRange = [0, 0]
N = 0
function = None
epsilon = 0.00001

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zadanie 4")
        self.root.minsize(1000, 750)

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

        self.label = tk.Label(self.root, text="Wprowadź N: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text2 = tk.Text(self.root, height=1, font=('Arial', 12))
        self.text2.pack()

        self.button3 = tk.Button(self.root, text="Wprowadź N", command=self.getN)
        self.button3.pack()

        self.label = tk.Label(self.root, text="Wprowadź epsilon: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text6 = tk.Text(self.root, height=1, font=('Arial', 12))
        self.text6.pack()

        self.button7 = tk.Button(self.root, text="Wprowadź epsilon", command=self.getEpsilon)
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

        self.label = tk.Label(self.root, text="Kwadratura Gaussa-Czybyszewa: ", font=('Arial', 18))
        self.label.pack(pady=10)

        self.text5 = tk.Text(self.root, height=4, font=('Arial', 12))
        self.text5.config(state="disabled")
        self.text5.pack()

        self.button6 = tk.Button(self.root, text="Oblicz całke", command=self.gaussChebyshevCalculate)
        self.button6.pack()

        self.button_authors = tk.Button(self.root, text="Autorzy", command=self.openPopup)
        self.button_authors.place(relx=0.95, rely=0.95, anchor="se")

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
        integralRange= [float(number.strip()) for number in numbers_as_strings]

    def printOriginalFunctionPlot(self):
        f = self.getFunction()
        x = np.linspace(-1, 1, 1000)
        # Wartosci funkcji
        y = f(x)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.plot(x, y)
        ax.grid()
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)
        plt.show()

    def getN(self):
        global N
        user_input = self.text2.get("1.0", tk.END)
        nAsString = user_input
        N = int(nAsString)
        return N

    def getEpsilon(self):
        global epsilon
        user_input = self.text6.get("1.0", tk.END)
        epsilonAsString = user_input
        epsilon = float(epsilonAsString)
        return epsilon


    def openPopup(self):
        popup = tk.Toplevel(self.root,)
        popup.title("Autorzy")
        popup.geometry("400x200")
        label = tk.Label(popup, text="Piotr Płeska 242499")
        label.pack(padx=20, pady=20)
        label = tk.Label(popup, text="Marcin Mazur 242467")
        label.pack(padx=20, pady=20)
        button = tk.Button(popup, text="Wyjdź", command=popup.destroy)
        button.pack(pady=10)

    def simpsonMethod(self):
        # trzeba dodac zachowanie co sie dzieje jak mamy integralRange inf obojetnie ktore
        global N
        n = N
        result = 1
        s = 0
        a = 0
        while math.fabs(result - s) > epsilon:
            a+=1
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

    def gaussChebyshevMetod(self, nodesAmount):
        # trzeba dodac obliczanie po zwiekszanym przedziale - to sa te granice
        # (nie mam pojecia gdzie w tym wzorze to mozna zrobic - wzor z wiki, ktora pokazywal)

        # jak juz sie doda to do gory to trzeba dodac tez porownywanie wyniku z epsilonem (tak jak w sampsonie)
        result = 0
        weight = math.pi / nodesAmount
        for i in range(1, nodesAmount+1):
            node = math.cos(((2 * i - 1) * math.pi) / (2 * nodesAmount))
            result += (self.calculateFunction(node))/(1/(math.sqrt(1-(node*node))))
        return weight * result

    def gaussChebyshevCalculate(self):
        self.text5.config(state="normal")
        self.text5.delete('1.0', 'end')
        for i in range(2,6):
            self.text5.insert(tk.END,"Liczba węzłow: " + str(i) + "  -  " + str(self.gaussChebyshevMetod(i))+"\n")
        self.text5.config(state="disabled")


GUI()

