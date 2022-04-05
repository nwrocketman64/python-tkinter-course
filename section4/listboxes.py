import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example: ListBoxes")

programmung_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

langs = tk.StringVar(value=programmung_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")
langs_select.pack()

root.mainloop()
