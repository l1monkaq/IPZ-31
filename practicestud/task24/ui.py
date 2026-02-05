import tkinter as tk

class AppWindow(tk.Tk):
    def __init__(self, logic_function):
        super().__init__()
        self.title("Аналізатор тексту")
        self.geometry("350x250")
        self.logic_function = logic_function

        tk.Label(self, text="Введіть ваш текст:", font=("Arial", 10)).pack(pady=10)
        self.input_field = tk.Entry(self, width=40)
        self.input_field.pack(pady=5)

        self.btn = tk.Button(self, text="Обробити", command=self._on_submit, bg="#e1e1e1")
        self.btn.pack(pady=15)

        self.result_label = tk.Label(self, text="Результат з'явиться тут", fg="blue")
        self.result_label.pack(pady=10)

    def _on_submit(self):
        data = self.input_field.get()
        result = self.logic_function(data)
        self.result_label.config(text=result)