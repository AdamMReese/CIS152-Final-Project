"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
" Name : Program Name
" Author: Adam Reese
" Created : " Course: CIS 152 - Data Structure
" Version: 1.0
" OS: Windows 11
" IDE: PyCharm 2023.2 (Professional Edition)
" Copyright : This is my own original work 
" based on specifications issued by our instructor
" Description : An app that .... ADD HERE....
"            Input: ADD HERE XXX
"            Output: ADD HERE XXX
" Academic Honesty: I attest that this is my original work.
" I have not used unauthorized source code, either modified or
" unmodified. I have not given other fellow student(s) access
" to my program.
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""
from tkinter import messagebox
from gui import init_gui


# Add an event handler for window closing
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()


if __name__ == "__main__":
    # Call the init_gui function from gui.py
    (
        root,
        products_listbox,
        status_var,
        simulate_distribution_button,
        clear_inventory_button,
    ) = init_gui()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Enter the main loop
    root.mainloop()
