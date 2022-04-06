import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Distance Converter")
        self.frames = dict()
        
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")
        
        feet_to_meters = FeetToMeter(container, self)
        feet_to_meters.grid(row=0, column=0, sticky="NSEW")
        
        meters_to_feet = MetersToFeet(container, self)
        meters_to_feet.grid(row=0, column=0, sticky="NSEW")
        
        self.frames[FeetToMeter] = feet_to_meters
        self.frames[MetersToFeet] = meters_to_feet
        
        #self.bind("<Return>", frame.calculate)
        #self.bind("<KP_Enter>", frame.calculate)
    
    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()


class MetersToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here")
        
        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Arial", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, text="Feet shown here", textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        switch_page_button = ttk.Button(self, text="Switch to feet conversion", command=lambda: controller.show_frame(FeetToMeter))
        
        meters_label.grid(row=0, column=0, sticky="W", padx=15, pady=15)
        meters_input.grid(row=0, column=1, sticky="EW", padx=15, pady=15)
        meters_input.focus()

        feet_label.grid(row=1, column=0, sticky="W", padx=15, pady=15)
        feet_display.grid(row=1, column=1, sticky="EW", padx=15, pady=15)

        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW", padx=15, pady=15)
        switch_page_button.grid(row=3, column=0, columnspan=2, sticky="EW")
    
    def calculate(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            pass


class FeetToMeter(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        
        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar(value="Meters shown here")
        
        feet_label = ttk.Label(self, text="Feet:")
        feet_input = ttk.Entry(self, width=10, textvariable=self.feet_value, font=("Arial", 15))
        meters_label = ttk.Label(self, text="Meters:")
        meters_display = ttk.Label(self, text="Meters shown here", textvariable=self.meters_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate)
        
        feet_label.grid(row=1, column=0, sticky="W", padx=15, pady=15)
        feet_input.grid(row=1, column=1, sticky="EW", padx=15, pady=15)
        feet_input.focus()
        
        meters_label.grid(row=0, column=0, sticky="W", padx=15, pady=15)
        meters_display.grid(row=0, column=1, sticky="EW", padx=15, pady=15)

        calc_button.grid(row=2, column=0, columnspan=2, sticky="EW", padx=15, pady=15)
    
    def calculate(self, *args):
        try:
            feet = float(self.feet_value.get())
            meters = feet / 3.28084
            self.meters_value.set(f"{meters:.3f}")
        except ValueError:
            pass


root = DistanceConverter()

root.columnconfigure(0, weight=1)

font.nametofont("TkDefaultFont").configure(size=15)

root.mainloop()
