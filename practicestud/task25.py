import tkinter as tk
from tkinter import colorchooser

def start_draw(event):
    global sx, sy, obj
    sx, sy = event.x, event.y
    if tool.get() == "line":
        obj = cv.create_line(sx, sy, sx, sy, fill=clr, width=2)
    else:
        obj = cv.create_oval(sx, sy, sx, sy, outline=clr, width=2)

def dragging(event):
    cv.coords(obj, sx, sy, event.x, event.y)

def choose_clr():
    global clr
    c = colorchooser.askcolor()[1]
    if c: clr = c

root = tk.Tk()
root.title("Малювалка 2026")
clr, sx, sy, obj = "blue", 0, 0, None
tool = tk.StringVar(value="line")

ctrl = tk.Frame(root)
ctrl.pack(pady=5)
tk.Radiobutton(ctrl, text="Лінія", variable=tool, value="line").pack(side="left")
tk.Radiobutton(ctrl, text="Коло", variable=tool, value="oval").pack(side="left")
tk.Button(ctrl, text="Колір", command=choose_clr).pack(side="left", padx=5)
tk.Button(ctrl, text="Очистити", command=lambda: cv.delete("all")).pack(side="left")
tk.Button(ctrl, text="Зберегти", command=lambda: cv.postscript(file="draw.ps")).pack(side="left")

cv = tk.Canvas(root, width=600, height=400, bg="white")
cv.pack()
cv.bind("<Button-1>", start_draw)
cv.bind("<B1-Motion>", dragging)

root.mainloop()