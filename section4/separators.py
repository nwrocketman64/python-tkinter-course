import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example: Separators")

ttk.Label(root, text="Hello, world!", padding=20).pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

ttk.Label(root, text="Hello, world!", padding=20).pack()

root.mainloop()
