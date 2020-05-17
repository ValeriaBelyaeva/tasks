# дроби
from math import gcd
from functools import total_ordering

@total_ordering
class Fraction:

    def __init__(self, num, denum=1):
        if isinstance(num, str):
            num, denum = map(int, num.split('/'))
        num // denum  # if denum == 0 -> error
        if num != 0:
            self.sign = num * denum // abs(num * denum)  # +-1
        else:
            self.sign = 1
        obj_gcd = gcd(num, denum)
        self.num = abs(num) // obj_gcd
        self.denum = abs(denum) // obj_gcd

    def __str__(self):
        to_print = ''
        if self.sign == -1:
            to_print += '-'
        if self.num >= self.denum:
            to_print += '{}'.format(self.num // self.denum)

        if self.num >= self.denum and self.num % self.denum != 0:
            to_print += ' and '

        if self.num % self.denum != 0:
            to_print += '{}/{}'.format(self.num % self.denum, self.denum)
        return to_print

    def red(self):
        self.num = int(self.num)
        self.denum = int(self.denum)
        return Fraction(self.num // gcd(self.num, self.denum), self.denum // gcd(self.num, self.denum))

    def __repr__(self):
        return 'Fraction({}, {}, {})'.format(self.num, self.denum, self.sign)

    def __add__(self, second):
        if isinstance(second, int):
            second = Fraction(second)
        new_num = self.sign * self.num * second.denum + second.sign * self.denum * second.num
        new_denum = self.denum * second.denum
        return Fraction(new_num, new_denum)

    def __radd__(self, second):
        return self + second

    def __neg__(self):
        return Fraction(self.sign * self.num * (-1), self.denum)

    def __sub__(self, second):
        return self + (-second)

    def __rsub__(self, second):
        pass

    def __lt__(self, second):
        return self.sign * self.num * second.denum < second.sign * self.denum * second.num

    def __eq__(self, second):
        return not (self < second or second < self)

    def __int__(self):
        return self.sign * (self.num // self.denum)

    def __pow__(self, power):  # ______________________________задание 1, урок 15_____________________
        try:
            return Fraction(self.num ** power, self.denum ** power)
        except TypeError:
            self.num, self.denum = self.denum, self.num
            power *= -1
            return Fraction(self.num ** power, self.denum ** power)

    def __mul__(self, b):
        if isinstance(b, int):
            gcd_int = gcd(b, self.denum)
            if gcd_int > 1:
                return Fraction(self.num * (b // gcd_int), self.denum // gcd_int)
            else:
                return Fraction(self.num * b, self.denum)
        elif isinstance(b, Fraction):
            num = self.num * b.num
            demun = self.denum * b.denum
            return Fraction(num // gcd(num, demun), demun // gcd(num, demun))

    def myFloat(self):  # _________________________________________задание 2, урок 15_________________
        ans = str(self.sign * (self.num // self.denum)) + "."
        l = {}
        index = 0
        self.num = self.num % self.denum
        l[self.num] = index
        t = False
        while t == False:
            if self.num == 0:
                break
            digit = self.num * 10 // self.denum
            self.num = self.num * 10 - (self.num * 10 // self.denum) * self.denum
            if self.num not in l:
                ans += str(digit)
                index += 1
                l[self.num] = index
                t = False
            else:
                ans += str(digit) + ")"
                ans = ans[:l.get(self.num) + len(ans[:ans.index(".") + 1])] + "(" + ans[l.get(self.num) + len(
                    ans[:ans.index(".") + 1]):]
                t = True
        return ans


a = Fraction(3, 7)

print("тест к заданию 1, урок 15: ")
print("тест 1, возведение 3/7  в степень 5:", a ** 5)
print("тест 2, возведение 3/7  в степень 0:", a ** 0)
print("тест 3, возведение 3/7  в степень -2:", a ** -2)

a = Fraction(2, 3)
b = Fraction(9, 5)
print()
print("тест к заданию 2, урок 15: ")
print("тест 1, приведение 9/5 к float:", b.myFloat())
print("тест 2, приведение 2/3 к float:", a.myFloat())
