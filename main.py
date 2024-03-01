import tkinter as tk
from handler import Handler

def main():
    window = tk.Tk()
    window.title("Paint")
    Handler(window)
    window.mainloop()

if __name__ == "__main__":
    main()