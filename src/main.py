import webbrowser  # to open button link
from pyperclip import copy  # to copy result
from tkinter import ttk  # to create button start GUI mainloop
from popup import show_popup  # to show popup after result is recieved
from time_handler import ConvertTime  # to pass inputs to convert time
from gui import root, hour_input, minute_input, period_input, format_input  # to get gui and inputs

# Function to pass values to conversion function
def button_press(hour, minute, period, format):
    # Get converted time from function
    converted = ConvertTime(hour.get(), minute.get(), period.get(), format.get())
    
    # Check for errors
    if converted[0] == -1:
        show_popup("Error", converted[1])
    elif converted[0] == 0:
        # Attempt to copy result to clipboard
        try:
            copy(converted[1])
            converted[1] += "\nResult has been copied to clipboard"
        except:
            converted[1] += "\nResult was not copied to clipboard."
        
        # Display time
        show_popup("Time converted", converted[1])
    else:
        show_popup("Error", "Something went wrong.")

# Create 'Convert' button and pass input values to function
input_list = [hour_input, minute_input, period_input, format_input]
convert_button = ttk.Button(root, text="Convert", command=lambda: button_press(*input_list))
convert_button.pack(pady=10)

# Create button to redirect to GitHub repository
repo_button = ttk.Button(root, text="Open Github Repo", command=lambda: webbrowser.open_new_tab("https://github.com/Ali246801232/GermanTime"))
repo_button.pack(pady=4)

# Start GUI event loop
root.mainloop()