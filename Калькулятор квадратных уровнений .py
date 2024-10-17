from tkinter import *
from math import *

root = Tk()
root.title('Окно')
root.geometry('500x400+500+200')

def number():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = (b ** 2) - (4 * a * c)
        if d > 0:
            x1 = round((-b + sqrt(d)) / (2 * a), 2)
            x2 = round((-b - sqrt(d)) / (2 * a), 2)
            text = f'Корни: {x1}, {x2}'
        elif d == 0:
            x = round(-b / (2 * a))
            text = f'Корень: {x}'
        else:
            text = 'Нет корней'
    except ValueError:
        text = 'Ошибка ввода'

    output.delete(1.0, END)
    output.insert(END, text)

frame = Frame(root, relief=RAISED)
frame.pack(fill=BOTH, expand=True)

entry_a = Entry(frame, width=5)
entry_a.grid(row=1, column=0, padx=(10, 0))
Label(frame, text="= a").grid(row=1, column=1)

entry_b = Entry(frame, width=5)
entry_b.grid(row=1, column=2)
Label(frame, text="= b").grid(row=1, column=3)

entry_c = Entry(frame, width=5)
entry_c.grid(row=1, column=4)
Label(frame, text="= c").grid(row=1, column=5)

btn = Button(frame, text='Решить', command=number)
btn.grid(row=1, column=6, padx=(25, 0))

output = Text(frame, bg='pink', font='Arial', width=50, height=30)
output.grid(row=2, columnspan=8)

root.mainloop()