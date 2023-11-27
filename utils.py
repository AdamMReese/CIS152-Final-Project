""" """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """
" Name : Utility Functions for Semiconductor Supply Chain Management
" Author: Adam Reese
" Created : 11/16/2023
" Course: CIS 152 - Data Structure
" Version: 1.0
" OS: Windows 11
" IDE: PyCharm 2023.5 (Professional Edition)
" Copyright : This is my own original work 
" based on specifications issued by our instructor
" Description : Utility functions supporting the Semiconductor Supply Chain Management app.
"            Input: Various data and parameters as required.
"            Output: Supportive functions for inventory management and GUI updates.
" Academic Honesty: I attest that this is my original work.
" I have not used unauthorized source code, either modified or
" unmodified. I have not given other fellow student(s) access
" to my program.
""" """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """ """

import tkinter as tk


# Class for the product inventory
class ProductInventory:
    def __init__(self):
        self.inventory = {}

    # Add a product to the inventory
    def add_product(self, product_id, product_info):
        product_info["id"] = product_id
        self.inventory[product_id] = product_info

    # Remove a product from the inventory
    def remove_product(self, product_id):
        del self.inventory[product_id]

    # Search for a product in the inventory
    def search_product(self, product_id):
        return self.inventory.get(product_id, "Product not found")

    # Get all products in the inventory
    def get_all_products(self):
        return self.inventory

    # Clear the inventory
    def clear_inventory(self):
        self.inventory.clear()


# Supplier Network Class
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# GUI-related functions
def update_product_list(listbox, product_inventory):
    if listbox and listbox.winfo_exists():
        listbox.delete(0, tk.END)
        all_products = product_inventory.get_all_products()

        # Sort the products by ID
        for product_id, product_info in all_products.items():
            product_id_str = f"ID: {product_id}"
            product_name = product_info.get("name", "Unknown Name")
            listbox.insert(tk.END, f"{product_id_str}, Name: {product_name}")
    else:
        print("Listbox does not exist or has been destroyed.")
