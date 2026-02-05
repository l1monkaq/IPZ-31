import tkinter as tk

def do_math(op):
    try:
        a = float(in1.get().replace(',', '.'))
        b = float(in2.get().replace(',', '.'))
        if op == '+': res = a + b
        elif op == '-': res = a - b
        elif op == '*': res = a * b
        elif op == '/': res = a / b
        out.config(text=f"Разом: {res:.2f}", fg="blue")
    except ZeroDivisionError:
        out.config(text="Ділення на 0!", fg="red")
    except ValueError:
        out.config(text="Введіть числа!", fg="red")

root = tk.Tk()
root.title("Мій Обчислювач")
root.geometry("300x250")

in1 = tk.Entry(root); in1.pack(pady=5)
in2 = tk.Entry(root); in2.pack(pady=5)

btns = tk.Frame(root); btns.pack(pady=10)
for char in "+-*/":
    tk.Button(btns, text=char, width=5, command=lambda c=char: do_math(c)).pack(side="left", padx=2)

out = tk.Label(root, text="Результату немає", font=("Arial", 12))
out.pack(pady=20)

root.mainloop()