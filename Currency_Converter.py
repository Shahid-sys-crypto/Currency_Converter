import json
import tkinter as tk
from tkinter import ttk

def load_data(file_path="currency.json"):
    try:
        with open(file_path,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def convert_currency(amount,from_currency,to_currency,rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    base_amount=amount/rates[from_currency]
    return base_amount*rates[to_currency]

def handle_conversion():
    try:
        amount=float(amount_entry.get())
        from_currency=from_entry.get().upper()
        to_currency=to_entry.get().upper()
        rates=load_data(file_path="currency.json")
        result=convert_currency(amount,from_currency,to_currency,rates)
        if result is not None:
            result_label.config(text=f"{amount}:{from_currency}     {to_currency}:{result:.2f}")
        else:
            result_label.config(text="conversion error")
    except ValueError:
        print("something went error")

root=tk.Tk()
root.title("currency converter")
root.geometry("500x350")

amount_label=tk.Label(root,text="Amount:",font=("Arial",10))
amount_label.pack(pady=10)

amount_entry=tk.Entry(root)
amount_entry.pack(pady=10)

from_label=tk.Label(root,text="From:",font=("Arial",10))
from_label.pack(pady=10)

from_entry=tk.Entry(root)
from_entry.pack(pady=10)

to_label=tk.Label(root,text="To:",font=("Arial",10))
to_label.pack(pady=10)

to_entry=tk.Entry(root)
to_entry.pack(pady=10)

convert_button=tk.Button(root,text="convert",command=handle_conversion)
convert_button.pack(pady=10)

result_label=tk.Label(root,text="",font=("Arial",10))
result_label.pack(pady=10)

root.mainloop()