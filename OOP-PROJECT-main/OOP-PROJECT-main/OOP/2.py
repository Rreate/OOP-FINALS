from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
        if order_entry.get().isdigit():
            order_total = float(order_entry.get())
            shipping_fee = shipping_var.get()

            if order_total < 0:
                raise ValueError("Order amount cannot be negative.")
            if shipping_fee == 0.0:
                raise ValueError("Please select a shipping option.")
            elif shipping_fee == 5.95 and order_total >= 75:
                shipping_fee = 0.0

            total = 1.12 * (order_total + shipping_fee)

            result_entry.delete(0, END)
            result_entry.insert(0, f"{total:.2f}")
        elif not order_entry.get().strip():
            raise ValueError("Order amount cannot have empty.")
        else:
            raise ValueError("Order amount cannot have letter.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


def clear_fields():
    order_entry.delete(0, END)
    result_entry.delete(0, END)
    shipping_var.set(0.0)


root = Tk()
root.geometry("1000x500")
root.resizable(False, False)

# --- Images ---

img_urs  = ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "University_of_Rizal.png")).resize((50, 50)))
img_cert = ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "Screenshot 2026-03-20 221441.png")).resize((80, 50)))
img_py   = ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "images.jpg")).resize((85, 60)))
img_bg   = ImageTk.PhotoImage(Image.open(os.path.join(BASE_DIR, "many-jars-of-candles-are-on-shelves-in-a-room-photo.jpg")).resize((1000, 500)))

root.columnconfigure(0, minsize=160)         
root.columnconfigure(1, weight=1)             
root.columnconfigure(2, minsize=120)        


bg_label = Label(root, image=img_bg)
bg_label.grid(row=0, column=0, columnspan=3, rowspan=10, sticky="nsew")
bg_label.lower()

logo_frame = Frame(root, bg="#f0f0e6")
logo_frame.grid(row=0, column=0, sticky="nw", padx=10, pady=20)
Label(logo_frame, image=img_urs,  bg="#f0f0e6").grid(row=0, column=0, padx=(0, 4))
Label(logo_frame, image=img_cert, bg="#f0f0e6").grid(row=0, column=1)

Label(root, image=img_py, bg="#f0f0e6").grid(row=0, column=2, sticky="ne", padx=10, pady=17)

panel = Frame(root, bg="#f0f0e6", bd=1, relief="solid", padx=20, pady=14)
panel.grid(row=0, column=1, sticky="n", pady=50)


panel.columnconfigure(0, weight=1)
panel.columnconfigure(1, weight=1)


Label(panel, text="CandleLine Corporation", bg="#f0f0e6",
      font=("Times New Roman", 20, "underline", "bold")
      ).grid(row=0, column=0, columnspan=2, pady=(0, 10))


Label(panel, text="Total amount of your order",
      bg="#f0f0e6", font=("Times New Roman", 10)
      ).grid(row=1, column=0, columnspan=2)


order_entry = Entry(panel, width=20, font=("Times New Roman", 10))
order_entry.grid(row=2, column=0, columnspan=2, pady=(2, 10))


Frame(panel, width=500, height=1, bg="black").grid(
    row=3, column=0, columnspan=2, sticky="ew", pady=(0, 6))


shipping_var = DoubleVar(value=0.0)
Label(panel, text="Shipping method", bg="#f0f0e6",
      font=("Times New Roman", 10)
      ).grid(row=4, column=0, columnspan=2, pady=(0, 4))



Radiobutton(panel, bg="#f0f0e6",
            text="Priority (overnight) @$14.95",
            value=14.95, variable=shipping_var,
            font=("Times New Roman", 10), anchor="w"
            ).grid(row=5, column=0, sticky="w", padx=10)

Radiobutton(panel, bg="#f0f0e6",
            text="Express (2 days) @$11.95",
            value=11.95, variable=shipping_var,
            font=("Times New Roman", 10), anchor="w"
            ).grid(row=5, column=1, sticky="w", padx=10)

Radiobutton(panel, bg="#f0f0e6",
            text="Standard (5 to 7 working days) @$5.95\n($0.00 if order amt > $75.00)",
            value=5.95, variable=shipping_var,
            wraplength=210, justify=LEFT,
            font=("Times New Roman", 10), anchor="w"
            ).grid(row=6, column=0, sticky="w", padx=10, pady=(0, 6))

Frame(panel, width=500, height=1, bg="black").grid(
    row=7, column=0, columnspan=2, sticky="ew", pady=6)

Label(panel, text="Amounts Payable (12% VAT included):",
      bg="#f0f0e6", font=("Times New Roman", 10)
      ).grid(row=8, column=0, sticky="e", padx=(0, 6), pady=6)

result_entry = Entry(panel, width=20, font=("Times New Roman", 10), bg="#DBDBD0")
result_entry.grid(row=8, column=1, sticky="w", pady=6)

btn_frame = Frame(panel, bg="#f0f0e6")
btn_frame.grid(row=9, column=0, columnspan=2, pady=(6, 0))
Button(btn_frame, text="Clear",   command=clear_fields).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Compute", command=compute_total).grid(row=0, column=1, padx=10)

root.mainloop()
