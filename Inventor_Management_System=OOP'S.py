# Project 7: Inventory Management System (OOP)
# Author: Mahesh Babu Doparthi

class Inventory:

    def __init__(self, product_name, product_id, price, stock):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.stock = stock

    def show_details(self):
        print("Product Name:", self.product_name)
        print("Product ID:", self.product_id)
        print("Price:", self.price)
        print("Stock:", self.stock)

    def update_price(self, price):
        self.price = price
        print("Price Updated Successfully!")
        print("Updated Price:", self.price)

    def add_stock(self, quantity):
        self.stock += quantity
        print("Stock Added Successfully!")
        print("Updated Stock:", self.stock)

    def sell_product(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print("Product Sold Successfully!")
            print("Remaining Stock:", self.stock)
        else:
            print("Out of Stock!")

    def check_product(self, product_id):
        if self.product_id == product_id:
            print("Product Found!")
        else:
            print("Product Not Found!")


# Creating Object

product1 = Inventory("Laptop", 101, 55000, 10)

print("========== PRODUCT DETAILS ==========")
product1.show_details()

print("\n========== UPDATE PRICE ==========")
product1.update_price(60000)

print("\n========== ADD STOCK ==========")
product1.add_stock(5)

print("\n========== SELL PRODUCT ==========")
product1.sell_product(3)

print("\n========== CHECK PRODUCT ==========")
product1.check_product(101)

print("\n========== UPDATED DETAILS ==========")
product1.show_details()