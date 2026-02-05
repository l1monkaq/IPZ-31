import tkinter as tk

def collect_data():
    if not agree.get():
        res.config(text="Помилка: прийміть умови!", fg="red")
        return
    info = f"Учасник: {name.get()}\nСтать: {sex.get()}"
    res.config(text=info, fg="blue")

root = tk.Tk()
root.title("Анкета учасника")

tk.Label(root, text="ПІБ:").grid(row=0, column=0, padx=5, pady=5)
name = tk.Entry(root)
name.grid(row=0, column=1)

sex = tk.StringVar(value="Чоловік")
tk.Label(root, text="Стать:").grid(row=1, column=0)
tk.Radiobutton(root, text="Чоловік", variable=sex, value="Чоловік").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Жінка", variable=sex, value="Жінка").grid(row=2, column=1, sticky="w")

agree = tk.BooleanVar()
tk.Checkbutton(root, text="Приймаю умови реєстрації", variable=agree).grid(row=3, columnspan=2)

tk.Button(root, text="Зберегти профіль", command=collect_data).grid(row=4, columnspan=2, pady=10)
res = tk.Label(root, text="", justify="left")
res.grid(row=5, columnspan=2)

root.mainloop()