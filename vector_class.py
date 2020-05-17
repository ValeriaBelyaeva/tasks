# вектор
class vector():
    def __init__(self, *args): # ___________________________________задание 3, урок 15___________
        self.args = args
        self.x = args[0] if len(args) >= 1 else 0
        self.y = args[1] if len(args) >= 2 else 0
        self.z = args[2] if len(args) >= 3 else 0

        self.space = len(args)

        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self): # ___________________________________задание 4, урок 15___________
        out = 'vector '
        if len(self.args) >= 1: out += "x: " + str(self.x)
        if len(self.args) >= 2: out += ", y: " + str(self.y)
        if len(self.args) >= 3: out += ", z: " + str(self.z)

        return out

    def scalar_product(self, b):  # ___________________________________задание 5, урок 15___________
        try:
            out = out = self.x * b.x
            if len(self.args) >= 2: out += self.y * b.y
            if len(self.args) >= 3: out += self.z * b.z
            return out
        except:
            return "TypeError: multiplier does not belong to the vector type"

    def angle(self, b):  # ___________________________________задание 5, урок 15___________
        from math import acos, degrees
        return degrees(acos(self.scalar_product(b) / (self.length * b.length)))

    def is_collinearity(self, b):  # ___________________________________задание 5, урок 15___________
        ans = []
        flag = 1
        if not (b.x == 0 == self.x):
            ans.append(b.x / self.x)
        if not (b.y == 0 == self.y):
            ans.append(b.y / self.y)
        if not (b.z == 0 == self.z):
            ans.append(b.z / self.z)

        if len(ans) - 1:
            for i in range(len(ans)):
                if ans[i] != ans[i - 1]: flag = 0

        if flag: return True
        return False

    def __eq__(self, b): # ___________________________________задание 6, урок 15___________
        if self.x == b.x and self.y == b.y and self.z == b.z:
            return True
        return False

    def __add__(self, b):
        return vector(self.x + b.x, self.y + b.y, self.z + b.z)

    def __radd__(self, b):
        return vector(self.x + b.x, self.y + b.y, self.z + b.z)

    def __sub__(self, b):
        return vector(self.x - b.x, self.y - b.y, self.z - b.z)

    def __mul__(self, b):
        try:
            return vector(self.x * b, self.y * b, self.z * b)
        except:
            return "TypeError: multiplier does not belong to the int or float type"

    def __lt__(self, b): # ___________________________________задание 6, урок 15___________
        if self.length < b.length:
            return True
        return False

    def __le__(self, b): # ___________________________________задание 6, урок 15___________
        if self.length <= b.length:
            return True
        return False

    def __gt__(self, b): # ___________________________________задание 6, урок 15___________
        if self.length > b.length:
            return True
        return False

    def __ge__(self, b): # ___________________________________задание 5, урок 15___________
        if self.length >= b.length:
            return True
        return False

    def __ne__(self, b): # ___________________________________задание 5, урок 15___________
        if self.x != b.x or self.y != b.y or self.z != b.z:
            return True
        return False

a = vector(2)
b = vector(5, 6)
c = vector(9, 4, 8)

print("тест к заданию 3 и 4, урок 15_______________ ")
print("тест 1:", a)
print("тест 2:", b)
print("тест 3:", c)

print()

print("тест к заданию 5, урок 15____________________")
print()
a1 = vector(2)
a2 = vector(-2)
a3 = vector(5)
print("вектор в одномерном промтранстве:")
print("тест 1, {} * {}:  ".format(a1, a2), a1.scalar_product(a2))
print("тест 2, {} * {}:  ".format(a1, a3), a1.scalar_product(a3))
print()
b1 = vector(5, 6)
b2 = vector(4, 8)
b3 = vector(-6, -4)
print("вектор в двумерном промтранстве:")
print("тест 3, {} * {}:  ".format(b1, b2), b1.scalar_product(b2))
print("тест 4, {} * {}:  ".format(b1, b3), b1.scalar_product(b3))
print()
c1 = vector(9, 4, 8)
c2 = vector(-6, -7, -1)
c3 = vector(7, 9, 2)
print("вектор в трёхмерном промтранстве:")
print("тест 5, {} * {}:  ".format(c1, c2), c1.scalar_product(c2))
print("тест 6, {} * {}:  ".format(c1, c3), c1.scalar_product(c3))

print()

print("тест к заданию 6, урок 15____________________")
print()
a1 = vector(2)
a2 = vector(-2)
a3 = vector(5)
print("вектор в одномерном промтранстве:")
print("тест 1, {} > {}:  ".format(a1, a2), a1 > a2)
print("тест 2, {} > {}:  ".format(a1, a3), a1 > a3)
print()

b1 = vector(5, 6)
b2 = vector(4, 8)
b3 = vector(-6, -4)
print("вектор в двумерном промтранстве:")
print("тест 3, {} > {}:  ".format(b1, b2), b1 > b2)
print("тест 4, {} > {}:  ".format(b1, b3), b1 > b3)
print()
c1 = vector(9, 4, 8)
c2 = vector(-6, -7, -1)
c3 = vector(6, 9, 10)
print("вектор в трёхмерном промтранстве:")
print("тест 5, {} > {}:  ".format(c1, c2), c1 > c2)
print("тест 6, {} > {}:  ".format(c1, c3), c1 > c3)

print()

#
# a = vector(2, 4, 7)
# b = vector(5, 3, 9)
# print(a.scalar_product(b))
# print(a.angle(b))
# print(a.is_collinearity(b))
