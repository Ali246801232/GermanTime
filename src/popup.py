import os  # for icon path manipulation
import sys  # for executable file compatibility
import tkinter as tk  # to create about popup
from tkinter import ttk  # to create button
from gui import root  # to create popup

# Function to display popup with message
def show_popup(title, message):
    # Create popup
    popup = tk.Toplevel()
    popup.title(title)
    popup.config(bg="#262626")
    popup.geometry("224x64")

    # Make sure new window is focused.
    popup.grab_set()
    popup.focus_set()

    # Create file path for window icon
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(os.path.dirname(sys.executable), "germantimeicon.ico")
    else:
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "germantimeicon.ico")

    # Set window icon
    popup.iconbitmap(icon_path)

    # Display popup message
    tk.Label(
        popup,
        text=message,
        background="#262626",
        foreground="white",
        font=("Helvetica", 10),
        wraplength=256
    ).pack()

    ok_button = ttk.Button(popup, text="OK", command=lambda: popup.destroy())
    ok_button.pack()

    popup.mainloop()
