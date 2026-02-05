from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno

file = None

def save():
    global file
    p = file or asksaveasfilename(defaultextension=".txt")
    if p:
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt.get("1.0", END))
        file = p
        root.title(f"Блокнот - {p}")

def open_f():
    global file
    p = askopenfilename()
    if p:
        file = p
        txt.delete("1.0", END)
        txt.insert("1.0", open(p, encoding="utf-8").read())
        root.title(f"Блокнот - {p}")

def on_close():
    if askyesno("Вихід", "Закрити програму? Переконайтеся, що зберегли зміни."):
        root.destroy()

root = Tk()
root.title("Блокнот")
root.geometry("600x400")

txt = Text(root, undo=True)
txt.pack(fill=BOTH, expand=1)

m = Menu(root)
root.config(menu=m)
fm = Menu(m, tearoff=0)
m.add_cascade(label="Файл", menu=fm)
fm.add_command(label="Відкрити", command=open_f)
fm.add_command(label="Зберегти", command=save)
fm.add_separator()
fm.add_command(label="Вийти", command=on_close)

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()