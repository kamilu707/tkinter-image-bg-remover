import tkinter as tk
from tkinter import filedialog

def process_files(file_paths):
    # Add your file processing logic here
    for file_path in file_paths:
        print(f"Processing file: {file_path}")

def browse_files():
    file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    process_files(file_paths)

# Create the main Tkinter window
root = tk.Tk()
root.title("File Processing App")

# Create a button to browse and select files
browse_button = tk.Button(root, text="Browse Files", command=browse_files)
browse_button.pack(pady=20)

# Create a button to start file processing
process_button = tk.Button(root, text="Process Files", command=lambda: process_files([]))
process_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()