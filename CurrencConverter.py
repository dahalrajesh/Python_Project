import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        root.title("Currency Converter")
        root.geometry("300x200")
        root.configure(padx=10, pady=10)

        # Exchange rate service
        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.75,
            "NPR": 116.0,  # Nepali Rupee rate
            "INR": 74.0,   # Indian Rupee rate
        }

        # Amount input
        tk.Label(root, text="Amount:").grid(row=0, column=0, pady=5, sticky="w")
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, pady=5)

        # "From" currency selection
        tk.Label(root, text="From:").grid(row=1, column=0, pady=5, sticky="w")
        self.from_currency = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.from_currency.grid(row=1, column=1, pady=5)
        self.from_currency.current(0)

        # "To" currency selection
        tk.Label(root, text="To:").grid(row=2, column=0, pady=5, sticky="w")
        self.to_currency = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.to_currency.grid(row=2, column=1, pady=5)
        self.to_currency.current(1)

        # Convert button
        convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result display
        tk.Label(root, text="Result:").grid(row=4, column=0, pady=5, sticky="w")
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=1, pady=5, sticky="w")

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()
            from_rate = self.exchange_rates[from_currency]
            to_rate = self.exchange_rates[to_currency]
            result = amount * (to_rate / from_rate)
            self.result_label.config(text=f"{result:.2f} {to_currency}")
        except ValueError:
            self.result_label.config(text="Invalid input!")
        except KeyError:
            self.result_label.config(text="Unknown currency!")
if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
