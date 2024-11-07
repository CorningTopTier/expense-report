import tkinter as tk
from tkinter import ttk

def submit_name(name_entry):
    name = name_entry.get()
    print("Name entered:", name)  # Or handle the name as needed
    return name  # Return the name for testing purposes

def create_app():
    # Create the main window
    root = tk.Tk()
    root.title("Name Input App")

    # Set window size
    root.geometry("300x150")

    # Label for the input
    label = ttk.Label(root, text="Enter your name:")
    label.pack(pady=10)

    # Entry widget for name input
    name_entry = ttk.Entry(root, width=30)
    name_entry.pack()

    # Button to submit
    submit_button = ttk.Button(root, text="Submit", command=lambda: submit_name(name_entry))
    submit_button.pack(pady=10)

    return root, name_entry  # Return root and name_entry for testing

if __name__ == "__main__":
    root, _ = create_app()
    root.mainloop()
