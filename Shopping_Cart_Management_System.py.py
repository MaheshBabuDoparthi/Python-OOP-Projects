# Project 11: Shopping Cart Management System
# Author: Mahesh Babu Doparthi

class Product:

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def show_details(self):
        print("🛒 Product Name:", self.product_name)
        print("💰 Price:", self.price)
        print("📦 Quantity:", self.quantity)

    def total_price(self):
        total = self.price * self.quantity
        print("💵 Total Price:", total)

    def increase_quantity(self, quantity):
        self.quantity += quantity
        print("✅ Quantity Updated Successfully!")
        print("Updated Quantity:", self.quantity)

    def remove_product(self):
        print("🗑️ Product Removed Successfully!")


cart = []

while True:

    print("\n========== Shopping Cart Management ==========")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Increase Quantity")
    print("4. Calculate Total Bill")
    print("5. Remove Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        product_name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        product = Product(product_name, price, quantity)
        cart.append(product)

        print("✅ Product Added Successfully!")

    elif choice == 2:

        if len(cart) == 0:
            print("🛒 Cart is Empty!")
        else:
            for product in cart:
                product.show_details()
                print("--------------------------")

    elif choice == 3:

        name = input("Enter Product Name: ")

        for product in cart:
            if product.product_name == name:
                quantity = int(input("Enter Quantity to Add: "))
                product.increase_quantity(quantity)
                break
        else:
            print("❌ Product Not Found!")

    elif choice == 4:

        grand_total = 0

        for product in cart:
            grand_total += product.price * product.quantity

        print("💵 Total Bill: ₹", grand_total)

    elif choice == 5:

        name = input("Enter Product Name: ")

        for product in cart:
            if product.product_name == name:
                cart.remove(product)
                product.remove_product()
                break
        else:
            print("❌ Product Not Found!")

    elif choice == 6:
        print("🙏 Thank You for Shopping!")
        break

    else:
        print("❌ Invalid Choice!")