# class shop():
    
#     def set_details(self, cust_name, prod_name, price, quantity):
#         self.cust_name = cust_name
#         self.prod_name = prod_name
#         self.price = price
#         self.quantity = quantity
        
        
#     def calculate_total(self):
#         total = self.price * self.quantity
#         return total

#     def apply_discount(self, discount):
#         total = self.calculate_total()
#         return total - (total * discount)
    
#     def display_all(self):
#         print(f"Total: {self.calculate_total()}")
#         print(f"Total after discount: {self.apply_discount(0.1)}")
        
# objj = shop()
# shop.set_details(objj, "John", "Laptop", 1000, 2)
# shop.display_all(objj)
# shop.set_details(objj, "Alice", "Phone", 500, 3)
# shop.display_all(objj)
        
        
# ----------------------------------------------------------------------

# class library():
    
#     def set_details(self, book_name, author, price):
#         self.book_name = book_name
#         self.author = author
#         self.price = price
        
#     def issue_book(self, member_name):
#         print(f"{member_name} has issued the book '{self.book_name}' by {self.author}.")

#     def return_book(self,member_name):
#         print(f"{member_name} has returned the book '{self.book_name}' by {self.author}.")
        
#     def display_details(self):
#         print(f"Book Name: {self.book_name}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
        
# obj = library()
# obj.set_details( "The Great Harshal", "Harshal", 5000)
# obj.issue_book("John")
# obj.return_book("John")
# obj.display_details()

# ----------------------------------------------------------------------

class electricity:
    
    def set_details(self,cust_name,unit_cunsumed):
        self.cust_name = cust_name
        self.unit_cunsumed = unit_cunsumed
    
    def calculate_bill(self):
        if self.unit_cunsumed <= 100:
            return self.unit_cunsumed*3
        elif self.unit_cunsumed <= 200:
            return self.unit_cunsumed*5
        else:
            return self.unit_cunsumed*8
    
    def display_bill(self):
        print(f"Customer Name: {self.cust_name}")
        print(f"Unit Consumed: {self.unit_cunsumed}")
        print(f"Total Bill: {self.calculate_bill()}")

obj = electricity()
obj.set_details("Harsh", 150)
obj.display_bill()

    