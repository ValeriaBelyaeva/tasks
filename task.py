# калькулятор
from tkinter import *
import time, random

WIDTH = 7
HEIGHT = 3
lbl = [('(', ')', 'C', '/'),
       ('1', '2', '3', '*'),
       ('4', '5', '6', '+'),
       ('7', '8', '9', '-'),
       ('0', '.', '**', '=')]

root = Tk()
columnsNum = len(lbl[0])
text = Text(width=18, height=2, font=("Verdana", 15))
text.grid(columnspan=columnsNum + 1)


def foo(st):
    if st == '=':
        tx = text.get('1.0', END)
        solver(tx)
    elif st == 'C':
        text.delete('1.0', END)
    else:
        text.insert(END, st)


joke = ['ЭВМ вычисляет...',
        "Минуточку....",
        'Хотите анекдот?',
        'Потише!\n Я тут считаю',
        "Вообще я нейросеть, а тут подрабатываю"]


def pr(out):
    text.delete('1.0', END)
    text.insert('1.0', out)


def solver(inp):
    out = str(eval(inp))
    if isinstance(eval(inp), float):  # round(eval(inp), 5)
        out = str(round(eval(inp), 10))
    text.delete('1.0', END)
    text.insert(END, random.choice(joke))
    text.after(2500, lambda: pr(out))  # after 1000ms


vijets = [[0, ] * len(lbl[0]) for _ in lbl]

for i in range(len(lbl)):
    for j in range(len(lbl[i])):
        vijets[i][j] = Button(root, text=lbl[i][j], width=WIDTH, height=HEIGHT, command=(lambda f=lbl[i][j]: foo(f)))
        vijets[i][j].grid(row=[i + 1], column=j + 1)

root.mainloop()
