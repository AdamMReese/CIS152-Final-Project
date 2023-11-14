import tkinter as tk
import webbrowser
from tkinter import messagebox

import folium
import numpy as np
from folium import Tooltip
from folium.plugins import MarkerCluster, AntPath
from tkinterweb import HtmlFrame as WebView

from utils import ProductInventory, update_product_list


class SupplierNetwork:
    def __init__(self):
        self.network = {}

    def add_supplier(self, supplier, products):
        self.network[supplier] = products

    def remove_supplier(self, supplier):
        del self.network[supplier]

    def get_all_suppliers(self):
        return self.network.keys()

    def get_supplier_products(self, supplier):
        return self.network[supplier]

    def clear_network(self):
        self.network = {}

    def search_supplier(self, supplier):
        return self.network.get(supplier, "Supplier not found")

    def get_all_products(self):
        products = [
            product for supplier in self.network for product in self.network[supplier]
        ]
        return products

    def get_all_suppliers_for_product(self, product):
        return [
            supplier for supplier in self.network if product in self.network[supplier]
        ]

    def get_all_products_for_supplier(self, supplier):
        return self.network[supplier]

    def get_all_products_for_all_suppliers(self):
        return [
            product for supplier in self.network for product in self.network[supplier]
        ]

    def get_all_suppliers_for_all_products(self):
        return list(self.network.keys())


# Facility functions
def get_source_facility(stage):
    source_facilities = {
        "Manufacturing": "Siltronic Corporation, Oregon",
        "Chip Design": "NUVIA Inc, California",
        "IP & EDA": "Arm Ltd, Texas",
        "Research & Development": "Albany NanoTech Complex, New York",
        "Sensor Integration": "TechHub Semiconductors, Nevada",
        "Material Research": "Global Materials Innovation, Arizona",
        "Microcontroller Design": "InnovateTech Labs, Colorado",
        "Simulation Development": "SimulCorp, Washington",
        # Add more stages and source facilities as needed
    }
    return source_facilities.get(stage, "Unknown Facility")


def get_destination_facility(stage):
    facility_map = {
        "Manufacturing": "Siltronic Corporation, Oregon",
        "Chip Design": "NUVIA Inc, California",
        "IP & EDA": "Arm Ltd, Texas",
        "Research & Development": "Albany NanoTech Complex, New York",
        "Sensor Integration": "TechHub Semiconductors, Nevada",
        "Material Research": "Global Materials Innovation, Arizona",
        "Microcontroller Design": "InnovateTech Labs, Colorado",
        "Simulation Development": "SimulCorp, Washington",
        # Add more stages and products as needed
    }
    return facility_map.get(stage, "Unknown Facility")


# Assuming you have facility_coordinates defined somewhere
facility_coordinates = {
    "Siltronic Corporation, Oregon": (45.57614, -122.7502),
    "NUVIA Inc, California": (37.3886, -121.9803),
    "Arm Ltd, Texas": (30.2436, -97.8460),
    "Albany NanoTech Complex, New York": (42.6909, -73.8334),
    "TechDistributors": (40.7128, -74.0060),
    "GlobalComponents": (34.0522, -118.2437),
    "InnovateTech": (39.7392, -104.9903),
    # Add more source facilities and coordinates as needed
}

# Define the ProductInventory instance globally
product_inventory = ProductInventory()

# Instantiate the SupplierNetwork
supplier_network = SupplierNetwork()

# Add fictional suppliers and their distribution centers
supplier_network.add_supplier("TechDistributors", ["WAFER001", "CHIP001", "IP001"])
supplier_network.add_supplier(
    "GlobalComponents", ["SENSOR001", "MATERIAL001", "MICROCHIP001"]
)
supplier_network.add_supplier("InnovateTech", ["RESEARCH001", "SIMULATION001"])

# Connect suppliers to facilities
supplier_network.network["TechDistributors"].extend(
    [{"source": "Siltronic Corporation, Oregon"}, {"source": "NUVIA Inc, California"}]
)
supplier_network.network["GlobalComponents"].append({"source": "Arm Ltd, Texas"})
supplier_network.network["InnovateTech"].append(
    {"source": "Albany NanoTech Complex, New York"}
)
supplier_network.network["GlobalComponents"].append(
    {"source": "Siltronic Corporation, Oregon"}
)


# Modify the simulate_distribution function
def simulate_distribution(
    supply_network, products_listbox, status_var, simulate_button, clear_button
):
    try:
        # Check if the manufacturing simulation has been performed
        if not product_inventory.get_all_products():
            status_var.set("Manufacturing simulation must be performed first.")
            return

        # List to store connections
        connections = []

        # Iterate over products in the inventory
        for product_id, product_info in product_inventory.get_all_products().items():
            # Ensure product_info has the "stage" key
            stage = product_info.get("stage", "Unknown")

            destination_facility = get_destination_facility(stage)
            source_facility = get_source_facility(stage)

            # Check if the source facility is known
            if source_facility:
                # Add the supplier and product to the supplier network
                supply_network.add_supplier(source_facility, [product_id])

                # Add the connection to the list
                connections.append((source_facility, destination_facility, product_id))

        update_product_list(products_listbox, product_inventory)
        status_var.set("Simulated distribution successfully!")

        # Enable the "Simulate Distribution" button after successful simulation
        simulate_button.config(state=tk.NORMAL)

        # Call the function without passing num_spokes to status_var.set
        generate_supply_chain_map(
            supply_network,
            facility_coordinates,
            status_var=status_var,
        )

        # Keep buttons enabled after distribution simulation
        simulate_button.config(state=tk.NORMAL)
        clear_button.config(state=tk.NORMAL)

        # Return the list of connections
        return connections

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        status_var.set("Error simulating distribution!")


# Modify the simulate_manufacturing function
def simulate_manufacturing(
    products_listbox, status_var, simulate_distribution_button, clear_inventory_button
):
    global product_inventory
    try:
        # Simulate manufacturing new products with stages
        new_products = [
            {"id": "WAFER001", "name": "Silicon Wafer", "stage": "Manufacturing"},
            {
                "id": "CHIP001",
                "name": "Integrated Circuit Chip",
                "stage": "Chip Design",
            },
            {"id": "IP001", "name": "Intellectual Property", "stage": "IP & EDA"},
            {
                "id": "RESEARCH001",
                "name": "Research Prototype",
                "stage": "Research & Development",
            },
            {"id": "SENSOR001", "name": "Sensor Module", "stage": "Sensor Integration"},
            {
                "id": "MATERIAL001",
                "name": "Advanced Material",
                "stage": "Material Research",
            },
            {
                "id": "MICROCHIP001",
                "name": "Microcontroller Chip",
                "stage": "Microcontroller Design",
            },
            {
                "id": "SIMULATION001",
                "name": "Simulation Software",
                "stage": "Simulation Development",
            },
            # Add more products with different stages as needed
        ]

        for product in new_products:
            product_id = product["id"]
            product_name = product["name"]

            # Check if the "stage" key exists in the product dictionary
            if "stage" in product:
                product_stage = product["stage"]
            else:
                product_stage = "Unknown Stage"

            # Ensure product_info is stored as a dictionary with required keys
            product_info = {
                "id": product_id,
                "name": product_name,
                "stage": product_stage,
            }
            product_inventory.add_product(product_id, product_info)

        update_product_list(products_listbox, product_inventory)
        status_var.set("Simulated manufacturing successfully!")

        # Enable the "Simulate Distribution" and "Clear Inventory" buttons
        simulate_distribution_button.config(state=tk.NORMAL)
        clear_inventory_button.config(state=tk.NORMAL)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        status_var.set("Error simulating manufacturing!")


# Define the visualize_distribution_on_map function
def generate_supply_chain_map(network, fac_coords, status_var):
    try:
        m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

        # Define colors for different types of facilities
        facility_colors = {
            "Siltronic Corporation, Oregon": "orange",
            "NUVIA Inc, California": "green",
            "Arm Ltd, Texas": "lightblue",
            "Albany NanoTech Complex, New York": "red",
            "TechDistributors": "purple",
            "GlobalComponents": "cadetblue",
            "InnovateTech": "pink",
            # Add more facilities and colors as needed
        }

        # Add markers for each facility
        marker_cluster = MarkerCluster().add_to(m)
        for facility, coords in fac_coords.items():
            folium.Marker(
                location=coords,
                popup=facility,
                icon=folium.Icon(color=facility_colors.get(facility, "blue")),
            ).add_to(marker_cluster)

        # Draw spokes from each distribution center to corresponding facilities
        for supplier in network.get_all_suppliers():
            source_coords = fac_coords.get(supplier)
            if source_coords:
                products = network.get_supplier_products(supplier)
                for product in products:
                    if "source" in product:
                        destination = get_destination_facility(product["stage"])
                        dest_coords = fac_coords.get(destination)
                        if dest_coords:
                            # Generate intermediary points (spokes)
                            spokes = generate_spokes(
                                source_coords,
                                dest_coords,
                                5,
                            )

                            # Draw PolyLine from distribution center to facility with arrows and tooltip
                            product_name = product.get("name", "Unknown Product")
                            tooltip_content = (
                                f"Product: {product_name}<br>Stage: {product['stage']}"
                            )
                            AntPath(
                                locations=[source_coords] + spokes + [dest_coords],
                                color="gray",
                                weight=2.5,
                                opacity=1,
                                tooltip=Tooltip(tooltip_content, sticky=True),
                                icons="arrow",
                            ).add_to(m)

        # Coordinates for each location
        coordinates = {
            "Silicon Wafer": [(45.57614, -122.7502), (40.7128, -74.0060)],
            "Integrated Circuit Chip": [(37.3886, -121.9803), (40.7128, -74.0060)],
            "Intellectual Property": [(30.2436, -97.8460), (40.7128, -74.0060)],
            "Research Prototype": [(42.6909, -73.8334), (37.7749, -122.4194)],
            "Sensor Module": [(36.1716, -115.1391), (40.7128, -74.0060)],
            "Advanced Material": [(34.0522, -118.2437), (34.0522, -118.2437)],
            "Microcontroller Chip": [(39.7392, -104.9903), (34.0522, -118.2437)],
            "Simulation Software": [(38.9072, -77.0369), (37.7749, -122.4194)],
        }

        # Add markers for each location
        for key, value in coordinates.items():
            folium.Marker(
                location=value[0],
                popup=key,
                icon=folium.Icon(color="blue"),
            ).add_to(m)

            # Add Multi-Polylines for each source-destination pair
            tooltip_content = f"Product: {key}"
            AntPath(
                locations=value,
                color="blue",
                weight=2.5,
                opacity=1,
                tooltip=Tooltip(tooltip_content, sticky=True),
                icons="arrow",
            ).add_to(m)

        # Save the map as an HTML file
        m.save("multi_polylines_map.html")
        webbrowser.open("multi_polylines_map.html")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        status_var.set("Error visualizing distribution on map!")


# Define a function to generate intermediary points (spokes)
def generate_spokes(start_coords, end_coords, number_spokes):
    start_point = np.array(start_coords)
    end_point = np.array(end_coords)

    # Generate equidistant points along the line connecting start and end points
    spokes = [
        tuple(start_point + (i / (number_spokes + 1)) * (end_point - start_point))
        for i in range(1, number_spokes + 1)
    ]

    return spokes


# Generate coordinates for spokes between facilities and distribution centers
def generate_coordinates_for_spokes(network, fac_coordinates, number_of_spokes):
    coordinates = []

    for supplier in network.get_all_suppliers():
        source_coords = fac_coordinates.get(supplier)
        if source_coords:
            products = network.get_supplier_products(supplier)
            for product in products:
                if "source" in product:
                    destination = get_destination_facility(product["stage"])
                    dest_coords = fac_coordinates.get(destination)
                    if dest_coords:
                        spokes = generate_spokes(
                            source_coords, dest_coords, number_of_spokes
                        )
                        coordinates.extend(spokes)

    return coordinates


# Add the function to embed the Folium map into Tkinter GUI using WebView
def embed_map_in_gui(html_path):
    root = tk.Tk()
    root.title("Embedded Folium Map")

    # Create a WebView component
    webview = WebView(root)
    webview.grid(row=0, column=0, sticky="nsew")

    # Load the Folium map HTML file into the WebView
    webview.load_url("file://" + html_path)

    root.mainloop()


if __name__ == "__main__":
    # Add your code to simulate manufacturing and distribution

    # Example coordinates for demonstration
    facility_coords = {
        "Siltronic Corporation, Oregon": (45.57614, -122.7502),
        "NUVIA Inc, California": (37.3886, -121.9803),
        # Add more coordinates as needed
    }

    # Generate coordinates for spokes
    num_spokes = 5  # Adjust as needed
    spokes_coordinates = generate_coordinates_for_spokes(
        supplier_network, facility_coords, num_spokes
    )
