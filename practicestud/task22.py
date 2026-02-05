import tkinter as tk
from tkinter import ttk, colorchooser

FILE = "color.txt"

def save_color(c):
    if c:
        root.config(bg=c)
        f1.config(bg=c); f2.config(bg=c); f3.config(bg=c)
        with open(FILE, "w") as f: f.write(c)

def load_color():
    try:
        with open(FILE, "r") as f: return f.read()
    except: return "#ffffff"

root = tk.Tk()
root.title("Tab System 2026")
root.geometry("400x300")

style = ttk.Style()
nb = ttk.Notebook(root)
nb.pack(fill="both", expand=True)

f1 = tk.Frame(nb); f2 = tk.Frame(nb); f3 = tk.Frame(nb)
nb.add(f1, text="Головна"); nb.add(f2, text="Налаштування"); nb.add(f3, text="Про нас")

tk.Label(f1, text="ПІБ:").pack(pady=10)
tk.Entry(f1).pack()

tk.Button(f2, text="Змінити фон", command=lambda: save_color(colorchooser.askcolor()[1])).pack(pady=50)

tk.Label(f3, text="Автор: Єва\nВерсія: 2.1 (2026)").pack(pady=40)

current_bg = load_color()
save_color(current_bg)

root.mainloop()