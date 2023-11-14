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

import tkinter as tk
from tkinter import messagebox
from supply_and_distribution import (
    SupplierNetwork,
    simulate_manufacturing,
    simulate_distribution,
)
from utils import ProductInventory, update_product_list

# Define the ProductInventory instance globally
product_inventory = ProductInventory()

# Instantiate the SupplierNetwork
supplier_network = SupplierNetwork()


# Define the open_instructions_window function
def open_instructions_window():
    instructions_window = tk.Toplevel()
    instructions_window.title("Instructions")

    instructions_label = tk.Label(
        instructions_window,
        text="Welcome to the Semiconductor Supply Chain Management System!\n\n"
        "Instructions:\n"
        "- Simulate Manufacturing: Simulate manufacturing new products.\n"
        "- Simulate Distribution: Simulate distributing products to suppliers.\n"
        "- Clear Inventory: Remove all products from the inventory.\n"
        "- Exit: Close the application.\n\n"
        "  Have fun exploring the supply chain!",
    )

    instructions_label.pack(padx=20, pady=20)

    # Close button
    close_button = tk.Button(
        instructions_window, text="Close", command=instructions_window.destroy
    )
    close_button.pack(pady=10)


# Define the clear_inventory function
def clear_inventory(
    products_listbox, status_var, clear_inventory_button, distribute_button
):
    try:
        product_inventory.clear_inventory()
        update_product_list(products_listbox, product_inventory)
        status_var.set("Inventory cleared successfully!")

        # Disable buttons after clearing inventory
        clear_inventory_button.config(state=tk.DISABLED)
        distribute_button.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        status_var.set("Error clearing inventory!")


# Define the main GUI function
def init_gui():
    try:
        # Create the main window
        main_window = tk.Tk()
        main_window.title("Semiconductor Supply Chain Management")

        # Set up the layout
        main_window.geometry("")  # No specific size, let it adjust based on contents

        # Center the window on the screen
        window_width = main_window.winfo_reqwidth()
        window_height = main_window.winfo_reqheight()
        position_right = int(main_window.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_window.winfo_screenheight() / 2 - window_height / 2)
        main_window.geometry("+{}+{}".format(position_right, position_down))

        # Row 0: Title label
        title_label = tk.Label(
            main_window,
            text="Semiconductor Supply Chain Management",
            font=("Helvetica", 16),
        )
        title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10), sticky="n")

        # Row 1: Products Listbox
        products_listbox = tk.Listbox(
            main_window, selectmode=tk.SINGLE, height=10, width=60
        )
        products_listbox.grid(
            row=1, column=0, columnspan=4, padx=20, pady=(10, 0), sticky="n"
        )

        # Row 3: Status label
        status_var = tk.StringVar()
        status_label = tk.Label(
            main_window, textvariable=status_var, fg="blue", anchor="center"
        )
        status_label.grid(
            row=3, column=0, columnspan=4, padx=20, pady=(10, 0), sticky="n"
        )

        # Row 7: Simulate Manufacturing button
        simulate_manufacturing_button = tk.Button(
            main_window,
            text="Simulate Manufacturing",
            command=lambda: simulate_manufacturing(
                products_listbox,
                status_var,
                simulate_distribution_button,
                clear_inventory_button,
            ),
            state=tk.NORMAL,
        )
        simulate_manufacturing_button.grid(
            row=7, column=0, columnspan=4, pady=(0, 10), sticky="n"
        )

        # Row 8: Simulate Distribution button
        simulate_distribution_button = tk.Button(
            main_window,
            text="Simulate Distribution",
            command=lambda: simulate_distribution(
                supplier_network,
                products_listbox,
                status_var,
                simulate_distribution_button,
                clear_inventory_button,
            ),
            state=tk.DISABLED,  # Disable this button by default
        )
        simulate_distribution_button.grid(
            row=8, column=0, columnspan=4, pady=(0, 10), sticky="n"
        )

        # Row 9: Clear Inventory button (initially disabled)
        clear_inventory_button = tk.Button(
            main_window,
            text="Clear Inventory",
            command=lambda: clear_inventory(
                products_listbox,
                status_var,
                clear_inventory_button,
                simulate_distribution_button,
            ),
            state=tk.DISABLED,  # Set to disabled initially
        )
        clear_inventory_button.grid(
            row=9, column=0, columnspan=4, pady=(0, 10), sticky="n"
        )

        # Add an exit button
        exit_button = tk.Button(main_window, text="Exit", command=main_window.destroy)
        exit_button.grid(row=11, column=0, columnspan=4, pady=10, sticky="s")

        # Instructions button in the bottom right corner
        instructions_button = tk.Button(
            main_window,
            text="?",
            command=open_instructions_window,
            font=("Helvetica", 14),
        )
        instructions_button.grid(row=11, column=3, padx=20, pady=(0, 20), sticky="se")

        # Configure row and column weights to center the widgets
        for i in range(12):
            main_window.grid_rowconfigure(i, weight=1)
        for i in range(4):
            main_window.grid_columnconfigure(i, weight=1)

        # Return products_listbox, status_var, simulate_distribution_button, and clear_inventory_button
        return (
            main_window,
            products_listbox,
            status_var,
            simulate_distribution_button,
            clear_inventory_button,
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return None, None
