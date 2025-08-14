import tkinter as tk
import random
import string

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry.delete(0, tk.END)
    entry.insert(0, password)
root = tk.Tk()
root.title("Random Strong Password Generator")
root.geometry("400x150")
root.resizable(False, False)  

entry = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
entry.pack(pady=15)

btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
btn.pack()

root.mainloop()
