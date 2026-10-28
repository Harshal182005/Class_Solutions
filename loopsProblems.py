# n = 12345
# rev = 0

# while (n>0):
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# print(rev)

#---------------------------------------------------------

# n = int(input("Enter a number -->"))

# rev = 0
# original = n
# while(n>0):
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if original == rev:
#     print("palindrome")
# else:
#     print("Not palindrome")

#-----------------ARMSTRONG NUMBER----------------------------------------

# n = 153
# original = n
# digit = len(str(n))
# sum = 0

# while n > 0:
#     rem = n % 10
#     sum = sum + rem ** digit
#     n = n // 10

# if sum == original:
#     print("Armstrong")
# else:
#     print("Not a armstrong number")

#-----------------Fibonacci NUMBER----------------------------------------

# n = int(input("Enter a number ---> "))

# a = 0
# b = 1

# print(a)
# print(b)

# for i in range(2, n):
#     next = a + b
#     a = b
#     b = next
#     print(b)


ctryInfo = [['NGP','PUNE'],['NASHIK','JALGAOn']]
for i in ctryInfo:
    print(i)