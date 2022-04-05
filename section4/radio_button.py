import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example: Radio Buttons")

storage_variable = tk.StringVar()

option_one = ttk.Radiobutton(
    root,
    text="Option 1",
    variable=storage_variable,
    value="First Option"
)

option_two = ttk.Radiobutton(
    root,
    text="Option 2",
    variable=storage_variable,
    value="Second Option"
)

option_three = ttk.Radiobutton(
    root,
    text="Option 3",
    variable=storage_variable,
    value="Third Option"
)

option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()