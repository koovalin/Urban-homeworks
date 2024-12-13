import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    result = num1 + num2
    insert_values(result)


def sub():
    num1, num2 = get_values()
    result = num1 - num2
    insert_values(result)


def mul():
    num1, num2 = get_values()
    result = num1 * num2
    insert_values(result)


def div():
    num1, num2 = get_values()
    result = num1 / num2
    insert_values(result)


x_buttons = 100
y_buttons = 220

window = tk.Tk()
window.title("Calculator")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=100, y=y_buttons)
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=y_buttons)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=y_buttons)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=y_buttons)

number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number1 = tk.Label(window, text="Введите первое число")
number1.place(x=100, y=50)

number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
number2 = tk.Label(window, text="Введите второе число")
number2.place(x=100, y=125)

answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)

window.mainloop()
