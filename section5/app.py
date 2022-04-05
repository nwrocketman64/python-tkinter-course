import tkinter as tk
import tkinter.font as font
from tkinter import ttk

root = tk.Tk()
root.title("Distance Converter")

root.columnconfigure(0, weight=1)

font.nametofont("TkDefaultFont").configure(size=15)

meters_value = tk.StringVar()
feet_value = tk.StringVar(value="Feet shown here")

def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


main = ttk.Frame(root, padding=(30, 15))
main.grid()

meters_label = ttk.Label(main, text="Meters:")
meters_input = ttk.Entry(main, width=10, textvariable=meters_value, font=("Arial", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet shown here", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meters_label.grid(row=0, column=0, sticky="W", padx=15, pady=15)
meters_input.grid(row=0, column=1, sticky="EW", padx=15, pady=15)
meters_input.focus()

feet_label.grid(row=1, column=0, sticky="W", padx=15, pady=15)
feet_display.grid(row=1, column=1, sticky="EW", padx=15, pady=15)

calc_button.grid(row=2, column=0, columnspan=2, sticky="EW", padx=15, pady=15)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
