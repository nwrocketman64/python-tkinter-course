import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example: ComboBoxes")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekday["state"] = "readonly"
weekday.pack()

root.mainloop()
