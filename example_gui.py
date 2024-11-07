import tkinter as tk
from tkinter import ttk

def main():
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
    def submit_name():
        name = name_entry.get()
        print("Name entered:", name)  # Or handle the name as needed

    submit_button = ttk.Button(root, text="Submit", command=submit_name)
    submit_button.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
