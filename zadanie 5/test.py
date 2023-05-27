import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import scipy

# def function(x):
#     return np.sin(x) # Example function: sin(x)
# def chebyshev_approximation(x, n, func):
#     coefficients = np.zeros(n + 1)  # Coefficients of Chebyshev polynomial terms
#     chebyshev_vals = np.polynomial.chebyshev.chebval(x, np.eye(n + 1)).T  # Evaluate Chebyshev polynomials at x
#     for i in range(n + 1):
#         coefficients[i] = np.dot(chebyshev_vals[i], func(x))  # Dot product of Chebyshev values and function values
#     return np.dot(coefficients, np.eye(n + 1)[0])
#
def plot_approximation(a, b, n):
    x = np.linspace(a, b, 100)  # x values for evaluation
    y = function(x)  # Original function values

    # approximation = np.array([chebyshev_approximation(xi, n, function) for xi in x])  # Approximate the function at each x
    approximation = [aproximation(x) for x in range(100)]

    plt.plot(x, y, label='Original Function')
    plt.plot(x, approximation, label='Approximation')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Chebyshev Polynomial Approximation')
    plt.show()


def function(x):
    return np.sin(x)

def coefficient(k):
    result, _ =(np.pi/2)* scipy.integrate.quad(lambda t: function(t) * Tk(k, t) * (1/np.sqrt(1-t*t)), -1, 1)
    return result

def Tk(n,x):
    return special.eval_chebyt(n, x)

def sth(k,t):
    return function(t) * Tk(k,t) *(1/np.sqrt(1-t*t))

# def rootsOfCheybshevPolinomial(n):
#     return special.roots_chebyt(n)[0];
# def something(k):
#     # print(function())
#     # print(CebyshevPolynomial(k, [x for x in rootsOfCheybshevPolinomial(k)]))
#     # print([1 / (np.sqrt(1 - x * x)) for x in rootsOfCheybshevPolinomial(k)])
#     return function([x for x in rootsOfCheybshevPolinomial(k)]) * CebyshevPolynomial(k,[x for x in rootsOfCheybshevPolinomial(k)]) * [1 / (np.sqrt(1 - x * x)) for x in rootsOfCheybshevPolinomial(k)]

n=3
def aproximation(x):
    sum = 0
    for i in range(n+1):
        sum+=coefficient(i)*Tk(i,x)
    return coefficient(0)/2 *Tk(0,x) + sum
def main():
    # print(coefficient(1))
    plot_approximation(-1,1,1)
    # print(rootsOfCheybshevPolinomial(2))
    # print(coefficient(1))


main()