import matplotlib.pyplot as plt
import numpy as np
import math


class Printer:
    def __init__(self,result,function,rangeL,rangeR):
        self.result = result
        self.function = function
        self.rangeL = rangeL
        self.rangeR = rangeR


    def printPlot(self):
        t = np.arange(self.rangeL, self.rangeR, 0.01)
        s = self.function(t)
        fig, ax = plt.subplots(figsize=(10, 7))
        ax.plot(t, s)
        ax.set(title='Wykres wybranej funkcji w podanym przedziale', xlabel='Miejsce zerowe funkcji: x = ' + str(self.result))
        ax.xaxis.label.set_size(18)
        ax.title.set_size(25)
        ax.plot(self.result, 0, 'o', color='red')
        ax.grid()
        ax.axhline(0, color='black', lw=2)
        ax.axvline(0, color='black', lw=2)
        plt.show()
