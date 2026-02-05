from ui import AppWindow
from logic import process_data

if __name__ == "__main__":
    app = AppWindow(process_data)
    app.mainloop()