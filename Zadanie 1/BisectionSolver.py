from Solver import Solver


class BisectionSolver(Solver):
    def __init__(self, function, rangeL, rangeR, epsilon,iterations):
        super(BisectionSolver, self).__init__(function, rangeL, rangeR, epsilon, iterations)

    def solveE(self):
        rangeL = self.rangeL
        rangeR = self.rangeR
        yL = self.function(rangeL)
        yR = self.function(rangeR)
        # print(yL)
        # print(yR)
        if yL * yR > 0:
            raise Exception("Nie ma miejsc zerowych lub wiele miejsc zerowych")
        while True:
            x0 = (rangeL + rangeR) / 2
            x = self.function(x0)
            if abs(x) < self.epsilon:
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
        if yL * yR > 0:
            raise Exception("Nie ma miejsc zerowych lub wiele miejsc zerowych")
        for i in range (self.iterations):
            x0 = (rangeL + rangeR) / 2
            x = self.function(x0)
            if x * self.function(rangeL) < 0:
                rangeR = x0
            else:
                rangeL = x0
                yL = self.function(x)
        return x0
