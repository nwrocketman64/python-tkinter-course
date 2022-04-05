import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Example: Labels")

label = ttk.Label(root, text="Hello, world!", padding=20)
label.config(font=("Arial", 20))
label.pack()

image = Image.open("download.png").resize((100, 100))
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, text="Image with text...", image=photo, padding=5, compound="right")
image_label.pack()

root.mainloop()
