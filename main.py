import tkinter as tk
from handler import Handler

def main():
    window = tk.Tk()
    Handler(window)
    window.mainloop()

if __name__ == "__main__":
    main()