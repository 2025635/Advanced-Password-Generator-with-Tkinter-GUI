import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Password Generator")
        self.master.geometry("400x300")
        
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack(pady=10)
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master, textvariable=self.password_var, width=30, state='readonly')
        self.password_entry.pack(pady=5)
        
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)
        
        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.pack(pady=5)
        
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Medium")  # Default value
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "Low", "Medium", "High")
        self.complexity_menu.pack()
        
    def generate_password(self):
        complexity = self.complexity_var.get()
        length = 12  # Default length
        
        if complexity == "Low":
            length = 8
            charset = string.ascii_letters + string.digits
        elif complexity == "Medium":
            length = 12
            charset = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "High":
            length = 16
            charset = string.ascii_letters + string.digits + string.punctuation
        
        generated_password = ''.join(random.choices(charset, k=length))
        self.password_var.set(generated_password)
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
