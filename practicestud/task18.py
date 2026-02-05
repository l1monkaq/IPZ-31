import tkinter as tk

root = tk.Tk()
root.title("Перша програма")
root.geometry("1024x768")
root.resizable(False, False)

tk.Label(root, text="Hello, world!", font=("Arial", 25)).pack(pady=100)
tk.Button(root, text="Закрити", command=root.destroy, width=15).pack()

root.mainloop()