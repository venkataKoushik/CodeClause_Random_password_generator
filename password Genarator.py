import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random password of specified length and character types.
    """
    # Create a list of characters to choose from based on user input
    chars = ''
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    # Generate a password by randomly selecting characters from the list
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_password_gui():
    """
    Displays a simple GUI for generating a random password.
    """
    # Create a new windowf
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("550x600")
    # Set the font size to 18
    font = ('Arial', 18)

    # Add a heading
    tk.Label(window, text="Password Generator", font=('Arial', 24), fg='cyan', bg='#222222').grid(row=0, column=0, columnspan=2, pady=20)

    # Set the background color to #222222
    window.configure(bg='#222222')
    
    # Add input fields for password length and character types
    tk.Label(window, text="Password length:", fg='deeppink', bg='#222222', font=font).grid(row=1, column=0, sticky="w", pady=10,padx=10)
    length_entry = tk.Entry(window, font=font)
    length_entry.insert(0, "8")
    length_entry.grid(row=1, column=1, pady=5)
    tk.Label(window, text="Use lowercase letters:", fg='deeppink', bg='#222222', font=font).grid(row=2, column=0, sticky="w", pady=10)
    lowercase_var = tk.BooleanVar()
    lowercase_var.set(True)
    lowercase_check = ttk.Checkbutton(window, variable=lowercase_var, text="", style='Accent.TCheckbutton', command=lambda: None)
    lowercase_check.grid(row=2, column=1, sticky="w", pady=5)
    tk.Label(window, text="Use uppercase letters:", fg='deeppink', bg='#222222', font=font).grid(row=3, column=0, sticky="w", pady=10)
    uppercase_var = tk.BooleanVar()
    uppercase_var.set(True)
    uppercase_check = ttk.Checkbutton(window, variable=uppercase_var, text="", style='Accent.TCheckbutton', command=lambda: None)
    uppercase_check.grid(row=3, column=1, sticky="w", pady=5)
    tk.Label(window, text="Use digits:", fg='deeppink', bg='#222222', font=font).grid(row=4, column=0, sticky="w", pady=10)
    digits_var = tk.BooleanVar()
    digits_var.set(True)
    digits_check = ttk.Checkbutton(window, variable=digits_var, text="", style='Accent.TCheckbutton', command=lambda: None)
    digits_check.grid(row=4, column=1, sticky="w", pady=5)
    tk.Label(window, text="Use symbols:", fg='deeppink', bg='#222222', font=font).grid(row=5, column=0, sticky="w", pady=10)
    symbols_var = tk.BooleanVar()
    symbols_var.set(True)
    symbols_check = ttk.Checkbutton(window, variable=symbols_var, text="", style='Accent.TCheckbutton', command=lambda: None)
    symbols_check.grid(row=5, column=1, sticky="w", pady=5)

    # Change the style of the checkboxes to change the highlight color
    style = ttk.Style()
    style.map("Accent.TCheckbutton",
              background=[('active', 'cyan'), ('selected', '#222222')],
              foreground=[('active', 'white'), ('selected', 'white')],
              highlightcolor=[('active', 'cyan'), ('selected', 'cyan')],
              highlightbackground=[('active', 'cyan'), ('selected', 'cyan')])

    # Increase the size of the generate button and change its color
    def generate():
        length = int(length_entry.get())
        use_lowercase = lowercase_var.get()
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    generate_button = tk.Button(window, text="Generate", command=generate, font=font, bg='cyan', fg='black')
    generate_button.grid(row=6, column=0, columnspan=2, pady=20)

    # Add a text entry to display the generated password
    tk.Label(window, text="Generated Password:", fg='deeppink', bg='#222222', font=font).grid(row=7, column=0,columnspan=1, pady=10)
    result_entry = tk.Entry(window, font=font)
    result_entry.grid(row=7, column=1, columnspan=1, pady=10)

    # Set the size of the generate button
    generate_button.config(width=8, height=1)

    # Run the window
    window.mainloop()

# Run the GUI
generate_password_gui()