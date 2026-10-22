# # # # # # # # # # # # # # username = "Abc@gmail.com"
# # # # # # # # # # # # # # password = "Abc@123"

# # # # # # # # # # # # # # if(username == "Abc@gmail.com"):
# # # # # # # # # # # # # #     if(password == "Abc@123"):
# # # # # # # # # # # # # #         print("Login Successful")
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         print("Incorrect Password")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("Incorrect Username")

# # # # # # # # # # # # # #<-------------------------------->

# # # # # # # # # # # # # age = 20
# # # # # # # # # # # # # candidate_reg = True
# # # # # # # # # # # # # if age >= 18:
# # # # # # # # # # # # #     if candidate_reg:
# # # # # # # # # # # # #         print("Registered to vote")
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #         print("Not registered to vote")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print("Not eligible to vote")
    
# # # # # # # # # # # # # #<-------------------------------->

# # # # # # # # # # # # score = 85
# # # # # # # # # # # # if score >= 45:
# # # # # # # # # # # #     print("Passed")
# # # # # # # # # # # #     if score >= 75:
# # # # # # # # # # # #         print("Distinction")
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print("No Distinction")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("Failed")

# # # # # # # # # # #  #<-------------------------------->
 
# # # # # # # # # # # positive = 20
# # # # # # # # # # # if positive > 0:
# # # # # # # # # # #     if(positive % 2 == 0):
# # # # # # # # # # #         print("Positive Even Number")
# # # # # # # # # # #     else:
# # # # # # # # # # #         print("Positive Odd Number")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("Negative Number")

# # # # # # # # # # #<-------------------------------->

# # # # # # # # # # # age = 25
# # # # # # # # # # # salary = 50000
# # # # # # # # # # # if age >= 18:
# # # # # # # # # # #     print("Age requirement met")
# # # # # # # # # # #     if salary >= 30000:
# # # # # # # # # # #         print("Salary requirement met")
# # # # # # # # # # #         print("Eligible for loan")
# # # # # # # # # # #     else:
# # # # # # # # # # #         print("Salary requirement not met")
# # # # # # # # # # #         print("Not eligible for loan")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("Age requirement not met")
# # # # # # # # # # #     print("Not eligible for loan")

# # # # # # # # # # #<-------------------------------->

# # # # # # # # # # username = "Harshal@gmail.com"
# # # # # # # # # # password = "Harshal@123"
# # # # # # # # # # isActive = True
# # # # # # # # # # if username == "Harshal@gmail.com":
# # # # # # # # # #     if password == "Harshal@123":
# # # # # # # # # #         if isActive:
# # # # # # # # # #             print("Login Successful")
# # # # # # # # # #         else:
# # # # # # # # # #             print("Account is inactive")
# # # # # # # # # #     else:
# # # # # # # # # #         print("Incorrect Password")
# # # # # # # # # # else:
# # # # # # # # # #     print("Incorrect Username")

# # # # # # # # # #<-------------------------------->

# # # # # # # # # #<------------------E Block-------------------->

# # # # # # # # # num= 20
# # # # # # # # # if num >=10 and num <=50:
# # # # # # # # #     print("Number is in the range of 10 to 50")
# # # # # # # # # else:
# # # # # # # # #     print("Number is out of the range of 10 to 50")
    
# # # # # # # # #<-------------------------------->

# # # # # # # # num1 = 6
# # # # # # # # if num1 % 3 == 0 and num1 % 7 == 0:
# # # # # # # #     print("Number is divisible by both 3 and 7")
# # # # # # # # else:
# # # # # # # #     print("Number is not divisible by both 3 and 7")

# # # # # # # # #<-------------------------------->

# # # # # # # age = 26
# # # # # # # if age >=21 and age <=35 :
# # # # # # #     print("Eligible for job")
# # # # # # # else:
# # # # # # #     print("Not eligible for job")

# # # # # # # #<-------------------------------->

# # # # # # a = "a"
# # # # # # if(a == "a" or a == "e" or a == "i" or a == "o" or a == "u"):
# # # # # #     print("Vowel")
# # # # # # else:
# # # # # #     print("Consonant")

# # # # # # #<-------------------------------->

# # # # # num1 = 202
# # # # # if not (num1 >= 100 and num1 <=200):
# # # # #     print("Number is out of the range of 100 to 200")
# # # # # else:
# # # # #     print("Number is in the range of 100 to 200")

# # # # # #<-------------------------------->

# # # # theory = True
# # # # practical = True
# # # # if theory and practical:
# # # #     print("Eligible for exam")
# # # # else:
# # # #     print("Not eligible for exam")

# # # # #<-------------------------------->

# # # amt = 600
# # # premium = True

# # # if amt >= 500 or premium:
# # #     print("Eligible for discount")
# # # else:
# # #     print("Not eligible for discount")
    
# # # #<-------------------------------->

# #  #<---------------F Block----------------->
# #  
# #           
# # a,b,c,d = 10,200,30,40
# # if a > b and a > c and a > d:
# #     print("a is the largest number")
# # elif b > a and b > c and b > d:
# #     print("b is the largest number")
# # elif c > d and c > a and c > b:
# #     print("c is the largest number")
# # else:
# #     print("d is the largest number")
    
# #<-------------------------------->

# # unit = 5
# # bill = 0

# # if unit <= 100:
# #     bill = unit *2
# # elif unit <=200:
# #     bill = (100*2)+((unit-100)*3)
# # else:
# #     bill = (100*2)+(100*3)+((unit-200)*5)
    
# # print("total electricity bill", bill)

# # grade = input("Enter your grade (A, B, C, or D): ").upper()

# # match grade:
# #     case "A":
# #         print("Excellent")
# #     case "B":
# #         print("Good")
# #     case "C":
# #         print("Average")
# #     case "D":
# #         print("Needs improvement")
# #     case _:
# #         print("Invalid grade")


# #<-------------------------------->

# month = input("Enter a month: ").strip().lower()

# match month:
#     case "january" | "february" | "march":
#         print("Quarter 1")
#     case "april" | "may" | "june":
#         print("Quarter 2")
#     case "july" | "august" | "september":
#         print("Quarter 3")
#     case "october" | "november" | "december":
#         print("Quarter 4")
#     case _:
#         print("Invalid month")


# #<-------------------------------->

# module = 1

# match module:
#     case 1:
#         print("User Module")
#     case 2 :
#         print("Admin Module")
#     case 3 :
#         print("Student Module")
#     case 4 :
#         print("Teacher Module")
#     case _:
#         print("Page not found!!")

oper = input("Enter any operator (+,-,*,/)")
a = 10
b = 20

match oper:
    case "+" :
        print(F"Addition of {a} + {b} =",a+b)
    case "-":
        print(F"Substraction of {a}-{b} = ",a-b)
    case "*":
        print(F"Multiplication of {a} * {b} = ",a*b)
    case "/":
        print(F"Division of {a} / {b} =",a/b)
    case _:
        print("Not valid")