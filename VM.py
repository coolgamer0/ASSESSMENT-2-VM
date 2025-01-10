# Vending Machine Program
# This program simulates a vending machine with categories, money management, suggestions, and stock management

print("Welcome to the Vending machine")
class VendingMachine:
    def __init__(self, currency_symbol='$', currency_name="USD"):
        # Vending machine items with their categories, prices, and stock quantities
        self.items = {
            'C1': {'name': 'Coke', 'category': 'Cold Drinks', 'price': 1.50, 'stock': 10},
            'C2': {'name': 'Sprite', 'category': 'Cold Drinks', 'price': 1.40, 'stock': 8},
            'C3': {'name': 'Water', 'category': 'Cold Drinks', 'price': 1.00, 'stock': 12},
            'S1': {'name': 'Chips', 'category': 'Snacks', 'price': 1.20, 'stock': 5},
            'S2': {'name': 'Chocolate', 'category': 'Snacks', 'price': 1.50, 'stock': 7},
            'S3': {'name': 'Biscuits', 'category': 'Snacks', 'price': 1.30, 'stock': 6},
            'H1': {'name': 'Coffee', 'category': 'Hot Drinks', 'price': 2.00, 'stock': 4},
            'H2': {'name': 'Tea', 'category': 'Hot Drinks', 'price': 1.80, 'stock': 3}
        }
        self.balance = 0.0
        self.currency_symbol = currency_symbol  # Allow the user to specify the currency symbol
        self.currency_name = currency_name  # Allow the user to specify the currency name (e.g., USD, AED)

    def display_menu(self):
        print(f"Welcome to the Vending Machine ({self.currency_name})!\n")
        print("Categories: Cold Drinks, Snacks, Hot Drinks")
        print("Please select an item by entering the code.")

        # Group items by category
        categories = ['Cold Drinks', 'Snacks', 'Hot Drinks']
        for category in categories:
            print(f"\n{category}:")
            for code, item in self.items.items():
                if item['category'] == category:
                    print(f"{code}: {item['name']} - {self.currency_symbol}{item['price']:.2f} - Stock: {item['stock']}")

    def get_money(self):
        try:
            self.balance = float(input(f"Please insert money ({self.currency_symbol}): "))
            if self.balance <= 0:
                print("Please insert a positive amount.")
                self.get_money()
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            self.get_money()

    def purchase_item(self):
        self.display_menu()
        selection = input("Enter the code of the item you want to buy: ").upper()

        if selection not in self.items:
            print("Invalid selection. Please choose a valid item code.")
            return self.purchase_item()

        item = self.items[selection]
        
        if item['stock'] == 0:
            print(f"Sorry, {item['name']} is out of stock.")
            return self.purchase_item()

        if self.balance < item['price']:
            print(f"Insufficient funds. {item['name']} costs {self.currency_symbol}{item['price']:.2f}. Please insert more money.")
            return self.purchase_item()

        # Update balance and stock
        self.balance -= item['price']
        item['stock'] -= 1
        print(f"\n{item['name']} has been dispensed.")
        print(f"Your change: {self.currency_symbol}{self.balance:.2f}")
        
        # Suggest a related item based on purchase
        self.suggest_related_item(item['category'])

    def suggest_related_item(self, category):
        if category == 'Hot Drinks':
            suggestion = 'S3'  # Biscuits, because they pair well with hot drinks
            print("We suggest you also buy some biscuits to go with your hot drink!")
        elif category == 'Cold Drinks':
            suggestion = 'S2'  # Chocolate, because it pairs well with drinks
            print("How about some chocolate to enjoy with your drink?")
        elif category == 'Snacks':
            suggestion = 'H1'  # Coffee, because snacks go well with hot drinks
            print("You might also enjoy a coffee with your snacks.")
        else:
            suggestion = None
        
        if suggestion and self.items[suggestion]['stock'] > 0:
            print(f"Suggestion: {self.items[suggestion]['name']} - {self.currency_symbol}{self.items[suggestion]['price']:.2f}")
        print("\n")

    def run_machine(self):
        while True:
            self.get_money()
            self.purchase_item()
            more_items = input("Would you like to buy another item? (yes/no): ").lower()
            if more_items != 'yes':
                print("Thank you for using the Vending Machine. Goodbye!")
                break

# Function to select currency
def select_currency():
    print("Please select your currency:")
    print("1. USD (US Dollar)")
    print("2. AED (United Arab Emirates Dirham)")
    print("3. AUD (Australian Dollar)")
    print("4. EUR (Euro)")

    choice = input("Enter the number corresponding to your currency: ")

    if choice == '1':
        return '$', 'USD'
    elif choice == '2':
        return 'AED', 'AED'
    elif choice == '3':
        return 'AUD', 'AUD'
    elif choice == '4':
        return '€', 'EUR'
    else:
        print("Invalid choice. Please try again.")
        return select_currency()

if __name__ == "__main__":
    # Select the currency before starting the machine
    currency_symbol, currency_name = select_currency()

    # Create a VendingMachine instance with the selected currency
    machine = VendingMachine(currency_symbol=currency_symbol, currency_name=currency_name)
    machine.run_machine()
