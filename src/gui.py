import os  # for icon path manipulation
import sys  # for executable file compatibility
import tkinter as tk  # to create GUI
from tkinter import ttk  # to use enhanced widgets

# Create root widget
root = tk.Tk()
root.title("GermanTime")
root.geometry("384x288")

# Create file path for window icon
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(os.path.dirname(sys.executable), "germantimeicon.ico")
else:
    icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "germantimeicon.ico")

# Set window icon
root.iconbitmap(icon_path)

# Set background colour
root.config(bg="#262626")

# Create base style
style = ttk.Style()
style.configure("TLabel", background="#262626", foreground="white")

# Display title
ttk.Label(root, text="Welcome to GermanTime!", style="TLabel", font=("Helvetica", 20)).pack()

# Create hour input box
ttk.Label(root, text="Hour (01 - 12):", style="TLabel").pack()
hour_input = ttk.Entry(root, width=35)
hour_input.pack()

# Create minute input box
ttk.Label(root, text="Minute (01 - 59):", style="TLabel").pack()
minute_input = ttk.Entry(root, width=35)
minute_input.pack()

# Create period input box
ttk.Label(root, text="Period (AM / PM):", style="TLabel").pack()
period_input = ttk.Entry(root, width=35)
period_input.pack()

# Create format input box
ttk.Label(root, text="Format (Numerical / Relative):", style="TLabel").pack()
format_input = ttk.Combobox(root, values=[
    "Numerical",
    "Relative"
], width=35)
format_input.set("Numerical")
format_input.pack()
