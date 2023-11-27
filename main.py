""" """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """
" Name : Semiconductor Supply Chain Manager
" Author: Adam Reese
" Created : 11/16/2023
" Course: CIS 152 - Data Structure
" Version: 1.0
" OS: Windows 11
" IDE: PyCharm 2023.5 (Professional Edition)
" Copyright : This is my own original work 
" based on specifications issued by our instructor
" Description : Main file for the Semiconductor Supply Chain Management app.
"            Input: User interactions with the GUI.
"            Output: GUI display and interactions with the supply chain simulation.
" Academic Honesty: I attest that this is my original work.
" I have not used unauthorized source code, either modified or
" unmodified. I have not given other fellow student(s) access
" to my program.
""" """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """

from tkinter import messagebox
from gui import init_gui


# Function to handle the user closing the window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()


if __name__ == "__main__":
    # Create the root window and set the title and size of the window
    (
        root,
        products_listbox,
        status_var,
        simulate_distribution_button,
        clear_inventory_button,
    ) = init_gui()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Start the main loop
    root.mainloop()
