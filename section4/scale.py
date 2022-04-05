import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example: Scales")

scale = ttk.Scale(root, orient="horizontal", from_=0, to=10)
scale.pack(fill="x")

root.mainloop()
