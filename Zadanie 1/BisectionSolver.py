from Solver import Solver


class BisectionSolver(Solver):
    def __init__(self, function, rangeL, rangeR, epsilon,iterations):
        super(BisectionSolver, self).__init__(function, rangeL, rangeR, epsilon, iterations)

    def solveE(self):
        licznik=0
        rangeL = self.rangeL
        rangeR = self.rangeR
        yL = self.function(rangeL)
        yR = self.function(rangeR)
        if yL * yR > 0:
            return "Nie ma miejsc zerowych lub jest ich więcej niż 1 w podanym przedziale"
        while True:
            licznik+=1
            x0 = (rangeL + rangeR) / 2
            x = self.function(x0)
            if abs(x) < self.epsilon:
                print(licznik)
                return x0
            if x * self.function(rangeL) < 0:
                rangeR = x0
            else:
                rangeL = x0
                yL = self.function(x)

    def solveI(self):
        yL = self.function(self.rangeL)
        yR = self.function(self.rangeR)
        rangeL = self.rangeL
        rangeR = self.rangeR
        n = int(self.iterations)
        if yL * yR > 0:
            return "Nie ma miejsc zerowych lub jest ich więcej niż 1 w podanym przedziale"
        for i in range(n):
            x0 = (rangeL + rangeR) / 2
            x = self.function(x0)
            if x * self.function(rangeL) < 0:
                rangeR = x0
            else:
                rangeL = x0
                yL = self.function(x)
        return x0
