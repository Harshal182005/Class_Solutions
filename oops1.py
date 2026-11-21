# class stud():
#     def set_details(self,name,rollno,course):
#         self.name = name
#         self.rollno = rollno
#         self.course = course
        
#     def show(self):
#         print(self.name)
#         print(self.rollno)
#         print(self.course)
        
# obj = stud()
# obj1 = stud()
# obj2 = stud()
# obj.set_details("Harsh",21,"Python")
# obj1.set_details("harshal",20,"Python")
# obj2.set_details("riya",22,"Python")
# obj.show()
# obj1.show()
# obj2.show()


# -------------------------------------------------

# class emp():
#     def set(self,name,salary):
#         self.name = name
#         self.salary = salary
        
#     def calc(self):
#         total_sal = self.salary * 12
#         print(total_sal)

# obj = emp()
# obj.set("Harsh",30000)
# obj.calc()

# -------------------------------------------------

# 3. Mobile Phone Details

# Create a Mobile class with brand, model and price.

# Create the following methods:
# - display_details()
# - apply_discount(discount)
#    Pass the discount amount as an argument and display the final price
# 

# class Mobile:

#     def __init__(self):
#         self.brand = "iPhone"
#         self.model = "IOS"
#         self.price = 125000

#     def display_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)

#     def apply_discount(self, discount):
#         final_price = self.price - discount
#         print("Final Price:", final_price)


# # Creating object
# m1 = Mobile()

# m1.display_details()
# m1.apply_discount(10000)

# -------------------------------------------------
# 4. Bank Account

# Create a BankAccount class with account holder name and balance.

# Create methods:
# - deposit(amount)
# - withdraw(amount)
# - display_balance()
#    Perform deposit and withdrawal operations.

# class BankAccount:

#     def __init__(self):
#         self.name = "Harshal"
#         self.balance = 1988888

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print("Withdrawal successful!")

#     def deposit(self, amount):
#         self.balance += amount
#         print("Amount deposited successfully!")

#     def display_balance(self):
#         print("Account holder:", self.name)
#         print("Current balance:", self.balance)


# obj = BankAccount()
# obj.display_balance()
# obj.deposit(5000)
# obj.withdraw(2000)
# obj.display_balance()

# # -------------------------------------------------
# 5. Car Rental System

# Create a Car class with car name, rent per day and number of rental days.

# Create a method calculate_rent() that accepts the number of days and calculates the total rental amount.
# Section 2: Constructors – No Args & Args

# class car():
     
#     def __init__(self):
#         self.car_name = "BMW"
#         self.rent = 1200
#         self.days = 10
    
#     def calculate_rent(self):
#         total = self.days * self.rent
#         return total
        
#     def display(self):
#         print("Car-->",self.car_name,"Total days car rented -->",self.days,"Total rent",self.calculate_rent())

# obj = car()
# obj.calculate_rent()
# obj.display()


# # -------------------------------------------------
# 7. Book Information – Parameterized Constructor

# Create a Book class with a parameterized constructor accepting:
# - Book name
# - Author name
# - Book price
#    Create two objects with different information.

# class book():
    
#     def __init__(self,b_name,a_name,b_price):
#         self.b_name = b_name
#         self.a_name = a_name
#         self.b_price = b_price
        
#     def display(self):
#         print("Book Name:",self.b_name)
#         print("Author Name:",self.a_name)
#         print("Book Price:",self.b_price)
        
# obj = book("The Great Harshal","Harshal",5000)
# obj1 = book("The Great Sahil","Sahil",5000)
# obj.display()
# obj1.display()

# 8. Rectangle Area

# Create a Rectangle class with a parameterized constructor accepting length and width.

# Create a method calculate_area() to calculate and display the area.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width

# obj = Rectangle(10, 5)
# area = obj.calculate_area()
# print("Area of the rectangle:", area)



# 9. Electricity Bill

# Create an ElectricityBill class with a parameterized constructor accepting:
# - Customer name
# - Units consumed
# Create a method calculate_bill() using the following conditions:
# - First 100 units: ₹5 per unit
# - Next 100 units: ₹7 per unit
# - Above 200 units: ₹10 per unit

# class ElectricityBill:
#     def __init__(self, customer_name, units_consumed):
#         self.customer_name = customer_name
#         self.units_consumed = units_consumed

#     def calculate_bill(self):
#         if self.units_consumed <= 100:
#             return self.units_consumed * 5
#         elif self.units_consumed <= 200:
#             return self.units_consumed * 7
#         else:
#             return (100 * 5) + (100 * 7) + ((self.units_consumed - 200) * 10)

#     def display_bill(self):
#         total_bill = self.calculate_bill()
#         print(f"Customer Name: {self.customer_name}")
#         print(f"Units Consumed: {self.units_consumed}")
#         print(f"Total Bill: ₹{total_bill}")

# obj = ElectricityBill("Harshal", 250)
# obj.display_bill()


# 10. Product Inventory

# Create a Product class with a parameterized constructor accepting product name, price and quantity.

# Create methods:
# - display_product()
# - calculate_total_price()
# - update_quantity(new_quantity)

# class Product:
#     def __init__(self, product_name, price, quantity):
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity

#     def display_product(self):
#         print(f"Product Name: {self.product_name}")
#         print(f"Price: ₹{self.price}")
#         print(f"Quantity: {self.quantity}")

#     def calculate_total_price(self):
#         total_price = self.price * self.quantity
#         return total_price

#     def update_quantity(self, new_quantity):
#         self.quantity = new_quantity
#         print(f"Updated Quantity: {self.quantity}")
        
# obj = Product("Laptop", 50000, 5)
# obj.display_product()
# print(f"Total Price: ₹{obj.calculate_total_price()}")
# obj.update_quantity(10)
# obj.display_product()


# 11. Company Employee Counter

# Create an Employee class with:
# - Class variable: company_name
# - Class variable: employee_count
# - Instance variables: employee_name, employee_id
#     Every time an object is created, increase the employee count by 1.

#     Display employee details and total employees.

# class Employee:
#     company_name = "Tech Solutions"
#     employee_count = 0

#     def __init__(self, employee_name, employee_id):
#         self.employee_name = employee_name
#         self.employee_id = employee_id
#         Employee.employee_count += 1

#     def display_employee(self):
#         print(f"Employee Name: {self.employee_name}")
#         print(f"Employee ID: {self.employee_id}")

    
#     def total_employees():
#         print(f"Total Employees: {Employee.employee_count}")
        
# obj1 = Employee("Harshal", 101)
# obj2 = Employee("Sahil", 102)
# obj1.display_employee()
# obj2.display_employee()
# Employee.total_employees()


# 12. School Student Information

# Create a Student class with:
# - Class variable: school_name
# - Instance variables: student_name, roll_number
# - Local variable inside a method: percentage
#     Create a method to display complete student information.
# class school:
#     school_name = "ABC School"

#     def __init__(self, student_name, roll_number):
#         self.student_name = student_name
#         self.roll_number = roll_number

#     def display_student_info(self, percentage):
#         print(f"School Name: {school.school_name}")
#         print(f"Student Name: {self.student_name}")
#         print(f"Roll Number: {self.roll_number}")
#         print(f"Percentage: {percentage}%")

# obj = school("Harshal", 21)
# obj.display_student_info(85)



# 14. Hospital Patient Management

# Create a Patient class with:
# - Class variable: hospital_name
# - Instance variables: patient_name, patient_age, disease
# Create a method display_patient() to display patient details.

#     Create three patient objects and display their information.

# class Patient:
#     hospital_name = "City Hospital"

#     def __init__(self, patient_name, patient_age, disease):
#         self.patient_name = patient_name
#         self.patient_age = patient_age
#         self.disease = disease

#     def display_patient(self):
#         print(f"Hospital Name: {Patient.hospital_name}")
#         print(f"Patient Name: {self.patient_name}")
#         print(f"Patient Age: {self.patient_age}")
#         print(f"Disease: {self.disease}")
# obj = Patient("Harshal", 21, "Flu")
# obj1 = Patient("Sahil", 22, "Cold")
# obj2 = Patient("Riya", 20, "Fever")
# obj.display_patient()
# obj1.display_patient()
# obj2.display_patient()




# 15. Online Course Management

# Create a Course class with:
# - Class variable: institute_name
# - Instance variables: course_name, course_fee
# - Local variable: discount
# Create a method calculate_fee() that calculates the final course fee after discount.
# Section 4: Methods, Arguments & Return Values

# class Course:
#     institute_name = "Online Academy"

#     def __init__(self, course_name, course_fee):
#         self.course_name = course_name
#         self.course_fee = course_fee

#     def calculate_fee(self, discount):
#         final_fee = self.course_fee - discount
#         return final_fee

#     def display_course(self, discount):
#         print(f"Institute Name: {Course.institute_name}")
#         print(f"Course Name: {self.course_name}")
#         print(f"Original Fee: ₹{self.course_fee}")
#         print(f"Discount: ₹{discount}")
#         print(f"Final Fee: ₹{self.calculate_fee(discount)}")
# obj = Course("Python Programming", 10000)
# obj.display_course(2000)



# 16. ATM Withdrawal System

# Create an ATM class with account holder name and balance.

# Create methods:
# - check_balance()
# - withdraw(amount)
# - deposit(amount)
#     The withdrawal method should accept an argument and return the updated balance.

# class ATM:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def check_balance(self):
#         return self.balance

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#             return self.balance
#         else:
#             self.balance -= amount
#             print(f"Withdrawal successful! New balance: ₹{self.balance}")
#             return self.balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposit successful! New balance: ₹{self.balance}")
#         return self.balance
# obj = ATM("Harshal", 5000)
# print(f"Current Balance: ₹{obj.check_balance()}")
# obj.withdraw(2000)
# obj.deposit(3000)




# 17. Temperature Converter

# Create a Temperature class with temperature in Celsius.

# Create methods:
# - celsius_to_fahrenheit()
# - fahrenheit_to_celsius(fahrenheit)
#     Return the converted temperature.

# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius

#     def celsius_to_fahrenheit(self):
#         fahrenheit = (self.celsius * 9/5) + 32
#         return fahrenheit

#     def fahrenheit_to_celsius(self, fahrenheit):
#         celsius = (fahrenheit - 32) * 5/9
#         return celsius
# obj = Temperature(25)
# print(f"Temperature in Fahrenheit: {obj.celsius_to_fahrenheit()}°F")
# obj2 = Temperature(0)  
# print(f"Temperature in Celsius: {obj2.fahrenheit_to_celsius(77)}°C")


# 18. Student Result Management

# Create a StudentResult class with student name and marks in three subjects.

# Create methods:
# - calculate_total()
# - calculate_percentage()
# - display_result()
#     Return total marks and percentage using methods.

# class StudentResult:
#     def __init__(self, student_name, marks):
#         self.student_name = student_name
#         self.marks = marks

#     def calculate_total(self):
#         return sum(self.marks)

#     def calculate_percentage(self):
#         total_marks = self.calculate_total()
#         percentage = (total_marks / (len(self.marks) * 100)) * 100
#         return percentage

#     def display_result(self):
#         total_marks = self.calculate_total()
#         percentage = self.calculate_percentage()
#         print(f"Student Name: {self.student_name}")
#         print(f"Total Marks: {total_marks}")
#         print(f"Percentage: {percentage:.2f}%")
# obj = StudentResult("Harshal", [85, 90, 78])
# obj.display_result()


# 19. Food Ordering System

# Create a FoodOrder class with:
# - Customer name
# - Food item
# - Food price
# - Quantity
# Create methods:
# - calculate_bill()
# - apply_coupon(discount)
# - display_order()
#     Calculate the final bill after applying the discount.

# class FoodOrder:
#     def __init__(self, customer_name, food_item, food_price, quantity):
#         self.customer_name = customer_name
#         self.food_item = food_item
#         self.food_price = food_price
#         self.quantity = quantity

#     def calculate_bill(self):
#         return self.food_price * self.quantity

#     def apply_coupon(self, discount):
#         total_bill = self.calculate_bill()
#         final_bill = total_bill - (total_bill * discount)
#         return final_bill

#     def display_order(self, discount=0):
#         total_bill = self.calculate_bill()
#         final_bill = self.apply_coupon(discount)
#         print(f"Customer Name: {self.customer_name}")
#         print(f"Food Item: {self.food_item}")
#         print(f"Price per Item: ₹{self.food_price}")
#         print(f"Quantity: {self.quantity}")
#         print(f"Total Bill: ₹{total_bill}")
#         print(f"Final Bill after {discount*100}% discount: ₹{final_bill}")
# obj = FoodOrder("Harshal", "Pizza", 500,2)
# obj.display_order(0.1)  


# 20. Vehicle Management System

# Create a Vehicle class with:
# - Class variable: vehicle_count
# - Instance variables: vehicle_name, vehicle_type, vehicle_price
# Create methods:
# - display_details()
# - calculate_insurance(rate)
# - update_price(new_price)
#     Count the total vehicles created and calculate insurance using the given rate.

class Vehicle:
    vehicle_count = 0

    def __init__(self, vehicle_name, vehicle_type, vehicle_price):
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type
        self.vehicle_price = vehicle_price
        Vehicle.vehicle_count += 1

    def display_details(self):
        print(f"Vehicle Name: {self.vehicle_name}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Vehicle Price: ₹{self.vehicle_price}")

    def calculate_insurance(self, rate):
        insurance_amount = self.vehicle_price * rate
        return insurance_amount

    def update_price(self, new_price):
        self.vehicle_price = new_price
        print(f"Updated Vehicle Price: ₹{self.vehicle_price}")

obj1 = Vehicle("Car", "Sedan", 1000000)
obj2 = Vehicle("Bike", "Sports", 500000)
obj1.display_details()
obj2.display_details()
print(f"Insurance for {obj1.vehicle_name}: ₹{obj1.calculate_insurance(0.05)}")
print(f"Insurance for {obj2.vehicle_name}: ₹{obj2.calculate_insurance(0.05)}")
obj1.update_price(1200000)
obj1.display_details()