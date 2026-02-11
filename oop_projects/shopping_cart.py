import os
import csv


class ShoppingCart:
    FILE_HEADERS = ["Item", "Price", "Quantity"]

    def __init__(self, filename: str):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        """Create file with headers if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.FILE_HEADERS)

    def add_item(self, item: str, price: float, quantity: int):
        """Add a new item to the cart."""
        try:
            with open(self.filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([item, price, quantity])
            print("✅ Item added successfully.")
        except Exception as e:
            print("❌ Error adding item:", e)

    def show_all_items(self):
        """Display all cart items."""
        if not os.path.exists(self.filename):
            print("⚠ No cart found.")
            return

        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            items = list(reader)

            if not items:
                print("🛒 Cart is empty.")
                return

            print("\n🛒 Shopping Cart")
            print("-" * 45)
            print(f"{'Item':<15}{'Price':<10}{'Quantity':<10}")
            print("-" * 45)

            for row in items:
                print(f"{row['Item']:<15}{row['Price']:<10}{row['Quantity']:<10}")

    def remove_item(self, item: str):
        """Remove item from cart."""
        if not os.path.exists(self.filename):
            print("⚠ File not found.")
            return

        with open(self.filename, "r", newline="") as file:
            rows = list(csv.DictReader(file))

        updated_rows = [row for row in rows if row["Item"].lower() != item.lower()]

        if len(rows) == len(updated_rows):
            print("⚠ Item not found.")
            return

        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.FILE_HEADERS)
            writer.writeheader()
            writer.writerows(updated_rows)

        print(f"✅ Item '{item}' removed successfully.")

    def total_price(self):
        """Calculate total cart value."""
        total = 0.0

        if not os.path.exists(self.filename):
            print("⚠ File not found.")
            return

        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total += float(row["Price"]) * int(row["Quantity"])

        print(f"💰 Total Cart Amount: ₹{total:.2f}")


# ---------------- MAIN PROGRAM ---------------- #

def main():
    cart = ShoppingCart("cart_data.csv")

    while True:
        print("\n📚 Shopping Cart Menu")
        print("1 ➤ Add Item")
        print("2 ➤ Remove Item")
        print("3 ➤ Show Total Price")
        print("4 ➤ View Cart")
        print("5 ➤ Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                item = input("Item name: ").strip()
                price = float(input("Item price: "))
                quantity = int(input("Quantity: "))
                cart.add_item(item, price, quantity)
            except ValueError:
                print("⚠ Invalid price or quantity.")

        elif choice == "2":
            cart.show_all_items()
            item = input("Item to remove: ").strip()
            cart.remove_item(item)

        elif choice == "3":
            cart.total_price()

        elif choice == "4":
            cart.show_all_items()

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("⚠ Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
