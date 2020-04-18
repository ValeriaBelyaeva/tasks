# уравнения
import math
class Equation:  # f(x) = 0

    def __init__(self, *function):
        self.function = function

    def func(self, a, b, x):
        return a * x - b

    def __str__(self):
        return '{}(x) = 0'.format(str(self.function))

    def __call__(self, x):
        return self.function(x)

    def solve(self, a, b):  # __________________________задание 4, урок 16_________
        result = set()
        for i in range(a, b):
            if self.func(self.function[0], self.function[1], i) == 0:
                result.add(i)
        return result


class СubicEquations():
    def __init__(self, *args):
        self.coefs = list(args)[::-1]
        self.a = self.coefs[3] if len(self.coefs) >= 4 else 0
        self.b = self.coefs[2] if len(self.coefs) >= 3 else 0
        self.c = self.coefs[1] if len(self.coefs) >= 2 else 0
        self.d = self.coefs[0] if len(self.coefs) >= 0 else 0

    def __getitem__(self, index):
        return self.coefs[index]

    def __setitem__(self, index, value):
        self.coefs[index] = value
        if index == 2:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            self.c = value

    def solve(self):   # __________________________задание 5, урок 16_________
        import numpy as num
        return list(num.roots(self.coefs[::-1]))


class PolynomialEquation(Equation):
    def __init__(self, *args):
        self.coefs = list(args)[::-1]

    def __str__(self):
        to_print = ' + {} = 0'.format(self.coefs[0])
        for i, coef in enumerate(self.coefs[1:]):
            if coef == 0:
                continue
            if coef < 0:
                to_print = ' - {}x^{}'.format(abs(coef), i + 1) + to_print
            else:
                to_print = ' + {}x^{}'.format(coef, i + 1) + to_print
        return to_print[2:]

    def __val(self, x):
        result = 0
        for i, coef in enumerate(self.coefs):  # 5x^2 + 4x + 1. x = 2
            result += coef * x ** i
        return result

    def __call__(self, x):
        return self.__val(x)

    def solve(self, a, b, c):  # __________________________задание 6, урок 16_________

        q = c - (a * b / 3) + (2 * a * a * a / 27)
        p = b - (a * a / 3)
        import math
        r = (-q / 2 + (q * q / 4 + p * p * p / 27)**0.5) ** (1 / 3)
        l = (-q / 2 - (q * q / 4 + p * p * p / 27)**0.5) ** (1 / 3)

        return r + l


print("______задание 6, урок 16_____________________________")
a = PolynomialEquation(4, 3, -7, 0)
print(*a.solve())

print("______задание 4, урок 16_____________________________")
a = Equation(5, 10)
print(a.solve(-1000, 1000))

print("_______задание 5, урок 16____________________________")
a = СubicEquations(-2, 8, 0)
print(*a.solve(-2, 8, 0))
