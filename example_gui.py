import tkinter as tk
from tkinter import ttk

# Function to handle name submission, with optional callback for test verification
def submit_name(name_entry, callback=None):
    name = name_entry.get()
    if callback:
        callback(name)  # Use callback for testing
    return name  # Return name for testing purposes

# Main function to create the app
def create_app(on_submit_callback=None):
    root = tk.Tk()
    root.title("Name Input App")
    root.geometry("300x150")

    # Label for the input
    label = ttk.Label(root, text="Enter your name:")
    label.pack(pady=10)

    # Entry widget for name input
    name_entry = ttk.Entry(root, width=30)
    name_entry.pack()

    # Button to submit, with callback for test
    submit_button = ttk.Button(
        root,
        text="Submit",
        command=lambda: submit_name(name_entry, on_submit_callback)
    )
    submit_button.pack(pady=10)

    return root, name_entry, submit_button

if __name__ == "__main__":
    root, _, _ = create_app()
    root.mainloop()
