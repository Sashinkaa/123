import tkinter as tk
from tkinter import messagebox


class ParkingSpot:
   

    def __init__(self, spot_number, location, base_price):
        self.spot_number = spot_number
        self.location = location
        self.__base_price = base_price

    def get_base_price(self):
        """Returns the base parking price."""
        return self.__base_price

    def set_base_price(self, new_price):
        
        if new_price > 0:
            self.__base_price = new_price
            return True
        else:
            return False

    def calculate_price(self, hours):
        
        return self.get_base_price() * hours


class PremiumParkingSpot(ParkingSpot):


    def __init__(self, spot_number, location, base_price, extra_fee):
        super().__init__(spot_number, location, base_price)
        self.extra_fee = extra_fee

    def calculate_price(self, hours):
     
        return (self.get_base_price() + self.extra_fee) * hours


normal_spot = ParkingSpot(1, "Ground floor", 2.0)

premium_spot = PremiumParkingSpot(
    2, "First floor", 2.0, 1.5
)

def display_information():
    normal_price = normal_spot.get_base_price()
    premium_price = premium_spot.get_base_price()

    information = f"""
=== NORMAL PARKING SPOT ===

Spot number: {normal_spot.spot_number}
Location: {normal_spot.location}
Price per hour: {normal_price:.2f} EUR
Total for 3 hours: {normal_spot.calculate_price(3):.2f} EUR


=== PREMIUM PARKING SPOT ===

Spot number: {premium_spot.spot_number}
Location: {premium_spot.location}
Price per hour: {premium_price:.2f} EUR
Extra fee: {premium_spot.extra_fee:.2f} EUR
Total for 3 hours: {premium_spot.calculate_price(3):.2f} EUR
"""

    output.delete("1.0", tk.END)
    output.insert(tk.END, information)


def change_price():
    try:
        new_price = float(price_entry.get())

        if normal_spot.set_base_price(new_price):
            messagebox.showinfo(
                "Success",
                "Base price successfully changed!"
            )
            display_information()
        else:
            messagebox.showerror(
                "Error",
                "Price must be greater than zero."
            )

    except ValueError:
        messagebox.showerror(
            "Invalid input",
            "Please enter a valid number."
        )


root = tk.Tk()
root.title("Car Parking System")
root.geometry("600x600")
root.configure(bg="#e8eef5")


title = tk.Label(
    root,
    text="CAR PARKING SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#e8eef5",
    fg="#1c3557"
)
title.pack(pady=15)


output = tk.Text(
    root,
    height=17,
    width=55,
    font=("Courier", 11),
    bg="white"
)
output.pack(pady=10)

display_information()


price_label = tk.Label(
    root,
    text="Enter new normal parking price (EUR/hour):",
    font=("Arial", 11),
    bg="#e8eef5"
)
price_label.pack(pady=5)

price_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)
price_entry.pack(pady=5)


change_button = tk.Button(
    root,
    text="Change Parking Price",
    font=("Arial", 11, "bold"),
    bg="#2878b5",
    fg="white",
    command=change_price
)
change_button.pack(pady=10)


exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 11, "bold"),
    bg="#c0392b",
    fg="white",
    command=root.destroy
)
exit_button.pack(pady=10)


root.mainloop()
