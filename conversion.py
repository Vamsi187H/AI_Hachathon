import tkinter as tk

from tkinter import filedialog, messagebox, scrolledtext

import re


# Handling user choice for file upload or manual input

def toggle_input_method():
    if choice.get() == 'upload':

        input_text.config(state='disabled')  # Disable input box for file upload

        load_button.config(state='normal')  # Enable file upload button

    elif choice.get() == 'manual':

        input_text.config(state='normal')  # Enable input box for manual input

        load_button.config(state='disabled')  # Disable file upload button


# Set up the main Tkinter window

root = tk.Tk()

root.title("Oracle SQL to EDB Converter")

root.geometry("900x700")

# --- Frame for User Choice (Upload or Manual Input) ---

choice_frame = tk.Frame(root)

choice_frame.pack(fill=tk.X, padx=10, pady=10)

choice_label = tk.Label(choice_frame, text="Choose Input Method:", font=("Arial", 12))

choice_label.pack(side=tk.LEFT)

choice = tk.StringVar(value="manual")  # Default choice is manual input

radio_upload = tk.Radiobutton(choice_frame, text="Upload SQL File", variable=choice, value="upload",
                              command=toggle_input_method, font=("Arial", 12))

radio_upload.pack(side=tk.LEFT, padx=10)

radio_manual = tk.Radiobutton(choice_frame, text="Enter SQL Script", variable=choice, value="manual",
                              command=toggle_input_method, font=("Arial", 12))

radio_manual.pack(side=tk.LEFT, padx=10)

# --- Frame for Input Section ---

input_frame = tk.Frame(root)

input_frame.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

input_label = tk.Label(input_frame, text="Oracle SQL Script", font=("Arial", 12, "bold"))

input_label.pack(anchor='w', pady=5)

input_text = scrolledtext.ScrolledText(input_frame, height=10, wrap=tk.WORD, font=("Arial", 10))

input_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# File Upload Button (inside Input Frame)

file_button_frame = tk.Frame(input_frame)

file_button_frame.pack(pady=5)

load_button = tk.Button(file_button_frame, text="Load Oracle SQL File", font=("Arial", 12), width=25, state='disabled')

load_button.grid(row=0, column=0, padx=5, pady=10)

# Convert Button (inside Input Frame)

convert_button = tk.Button(file_button_frame, text="Convert to EDB SQL", font=("Arial", 12), bg="lightblue", width=25)

convert_button.grid(row=0, column=1, padx=5, pady=10)

# --- Frame for Output Section ---

output_frame = tk.Frame(root)

output_frame.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

output_label = tk.Label(output_frame, text="Converted EDB SQL Script", font=("Arial", 12, "bold"))

output_label.pack(anchor='w', pady=5)

output_text = scrolledtext.ScrolledText(output_frame, height=10, wrap=tk.WORD, font=("Arial", 10))

output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# --- Frame for Action Buttons (Clear, Copy, Save) ---

button_frame = tk.Frame(root)

button_frame.pack(pady=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg="light grey", width=15)

clear_button.grid(row=0, column=0, padx=10)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", font=("Arial", 12), bg="light green", width=15)

copy_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(button_frame, text="Save EDB SQL File", font=("Arial", 12), bg="light yellow", width=15)

save_button.grid(row=0, column=2, padx=10)

# Start the Tkinter event loop

root.mainloop()
