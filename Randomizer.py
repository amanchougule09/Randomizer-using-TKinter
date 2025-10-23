import tkinter as tk
from tkinter import messagebox
import random

# ====== Generate Random Number Function ======
def generate_random():
    try:
        min_val = int(entry_min.get())
        max_val = int(entry_max.get())

        if min_val > max_val:
            messagebox.showerror("Invalid Range", "Minimum value cannot be greater than Maximum value.")
        else:
            number = random.randint(min_val, max_val)
            label_result.config(text=f"Random Number: {number}", fg="#470274")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

# ====== Hover Effects ======
def on_enter(e):
    generate_btn.config(bg="#470274", fg="white")

def on_leave(e):
    generate_btn.config(bg="#470274", fg="white")

# ====== Main Window ======
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("520x440")
root.configure(bg="#E9EEF6")


# ====== Shadow Effect ======
shadow = tk.Frame(root, bg="#C7C9D1")
shadow.place(relx=0.5, rely=0.5, anchor="center", width=396, height=326)

# ====== Main Frame ======
main_frame = tk.Frame(root, bg="#FFFFFF", bd=0, relief="flat")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=390, height=320)

# ====== Title ======
title_label = tk.Label(main_frame, text="Random Number Generator", font=("Poppins SemiBold", 14, "bold"), 
                       fg="#470274", bg="#FFFFFF")
title_label.pack(pady=15)

# ====== Input Fields ======
min_label = tk.Label(main_frame, text="Minimum Value", font=("Poppins", 10), bg="#FFFFFF", fg="#333333")
min_label.pack(pady=(5, 0))
entry_min = tk.Entry(main_frame, font=("Poppins", 11), relief="flat", justify="center",
                     bd=2, highlightthickness=1, highlightcolor="#470274",highlightbackground="#021732")
entry_min.pack(pady=5, ipady=4, ipadx=10)

max_label = tk.Label(main_frame, text="Maximum Value", font=("Poppins", 10), bg="#FFFFFF", fg="#333333")
max_label.pack(pady=(10, 0))
entry_max = tk.Entry(main_frame, font=("Poppins", 11), relief="flat", justify="center",
                     bd=2, highlightthickness=1, highlightcolor="#470274",highlightbackground="#021732")
entry_max.pack(pady=5, ipady=4, ipadx=10)

# ====== Generate Button ======
generate_btn = tk.Button(main_frame, text="Generate Number", font=("Poppins", 11, "bold"), bg="#470274", 
                         fg="white", activebackground="#470274", activeforeground="white", bd=0, 
                         relief="flat", padx=15, pady=8, cursor="hand2", command=generate_random)
generate_btn.pack(pady=15)

# Hover Bindings
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)

# ====== Result Label ======
label_result = tk.Label(main_frame, text="", font=("Poppins", 12, "bold"), bg="#FFFFFF", fg="#470274")
label_result.pack(pady=12)

# ====== Footer ======
footer_label = tk.Label(root, text="Designed by Aman", font=("Poppins", 9), bg="#E9EEF6", fg="#555555")
footer_label.pack(side="bottom", pady=5)

# ====== Run the App ======
root.mainloop()
