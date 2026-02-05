import tkinter as tk

def say_hi():
    msg.config(text="Привіт у системі!", fg="blue")

def reset():
    msg.config(text="")

root = tk.Tk()
root.title("Робоче вікно")
root.geometry("400x350")

msg = tk.Label(root, text="", font=("Verdana", 16))
msg.pack(pady=40)

tk.Button(root, text="Вітання", command=say_hi, width=20).pack(pady=5)
tk.Button(root, text="Очистити текст", command=reset, width=20).pack(pady=5)
tk.Button(root, text="Закрити програму", command=root.destroy, width=20, bg="#f0f0f0").pack(pady=20)

root.mainloop()