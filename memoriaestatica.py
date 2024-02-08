import tkinter as tk
from tkinter import simpledialog

def main():
    calificaciones = [0] * 5
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    for i in range(5):
        calificaciones[i] = int(simpledialog.askstring("Input", "captura la calificacion: "))
    root.destroy()

if __name__ == "__main__":
    main()

