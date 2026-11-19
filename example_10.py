# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# print(sum(1,2,3,4,5,6,7,8,9,10))


# def add(a,b):
#     print(a + b)
#     def sub(a,b):
#         print(a-b)
#         return 0
#     sub(10,5)
# print(add(10,5))


# def stud(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# stud(name="John", age=20, city="New York")


# def outer_function(a, b):
#     print(a + b)

#     def inner_function(a,b):
#         print(a*b)

#     inner_function(a, b)

# outer_function(10, 5)

# def SI(p,r,t):
#     return (p*r*t)/100
# print(SI(1000, 5, 2))


# def SI(**kwargs):
#     p = kwargs.get('p', 0)
#     r = kwargs.get('r', 0)
#     t = kwargs.get('t', 0)
#     print((p*r*t)/100)
# SI(p=1000, r=5, t=2)

# def cust(**kwargs):
#     for key,value in kwargs.items():
#         if key == "price":
#             total = 0
#             total += value
#     print(f"Total price: {total}")
        
# cust(name="John", price=85, city="New York")


# def total_marks(*args):
#     total = 0
#     for mark in args:
#         total += mark
#     return total
# total = total_marks(85, 90, 78, 92, 88)
# print(f"Total marks: {total}")

# def largest(*args):
#     largest = args[0]
#     for num in args:
#         if num > largest:
#             largest = num
#     return largest
# print(largest(10, 25, 5, 30, 15))

data = {}

while True:
    key = input("Enter a key (done if--- finished): ")
    if key =="done":
        break
    if key in data:
        print("Key already exists. Please enter a different key.")
        continue
    value = input("Enter a value: ")
    data[key] = value
    

print("Dictionary-------------->", data)
    
    
    
