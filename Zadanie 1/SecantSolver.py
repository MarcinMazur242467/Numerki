from Solver import Solver


class SecantSolver(Solver):

# prosta przez wykres fukcji na krancach przedziału
# obliczamy kandydata na miejsce zerowe
# zależenie od tego jakie sa znaki na lewo i prawo od miejsca zerowego

    def __init__(self, function, rangeL, rangeR, epsilon,iterations):
        super(SecantSolver, self).__init__(function, rangeL, rangeR, epsilon,iterations)


    def solveE(self):
        yL =  self.function(self.rangeL)
        yR = self.function(self.rangeR)
        rangeL = self.rangeL
        rangeR = self.rangeR
        while abs(rangeL - rangeR) > self.epsilon:
            x0 = rangeL -(yL*((rangeL-rangeR)/(yL-yR)))
            f0 = self.function(x0)
            if abs(f0) < self.epsilon:
                if x0 <= self.rangeR and x0>self.rangeL:
                    return x0
                else:
                    return "Brak miejsca zerowego w przedziale"
            rangeR = rangeL
            yR = yL
            rangeL = x0
            yL = f0

    def solveI(self):
        yL =  self.function(self.rangeL)
        yR = self.function(self.rangeR)
        rangeL = self.rangeL
        rangeR = self.rangeR

        i = int(self.iterations)
        while i > 0 :
            if yL - yR == 0:
                 return "Nie ma miejsc zerowych lub jest ich więcej niż 1 w podanym przedziale"
            x0 = rangeL -(yL*((rangeL-rangeR)/(yL-yR)))
            f0 = self.function(x0)
            rangeR = rangeL
            yR = yL
            rangeL = x0
            yL = f0
            i = i - 1
            if i == 0:
                if x0 <= self.rangeR and x0 > self.rangeL:
                    return x0
                else:
                    return "Brak miejsca zerowego w przedziale"