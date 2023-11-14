# utils.py
import tkinter as tk


# Product Inventory Class
class ProductInventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, product_info):
        product_info["id"] = product_id
        self.inventory[product_id] = product_info

    def remove_product(self, product_id):
        del self.inventory[product_id]

    def search_product(self, product_id):
        return self.inventory.get(product_id, "Product not found")

    def get_all_products(self):
        return self.inventory

    def clear_inventory(self):
        self.inventory.clear()


# Sorting Algorithm
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

        for product_id, product_info in all_products.items():
            product_id_str = f"ID: {product_id}"
            product_name = product_info.get("name", "Unknown Name")
            listbox.insert(tk.END, f"{product_id_str}, Name: {product_name}")
    else:
        print("Listbox does not exist or has been destroyed.")
