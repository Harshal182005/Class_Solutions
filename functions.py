# ============================================================
# 1. REVERSE A NUMBER
# ============================================================

# 1. With arguments, with return value
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
print("Reverse number:", reverse_number(1234))

# 2. With arguments, without return value
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print("Reverse number:", rev)
reverse_number(1234)

# 3. Without arguments, with return value
def reverse_number():
    n = int(input("Enter a number: "))
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
print("Reverse number:", reverse_number())

# 4. Without arguments, without return value
def reverse_number():
    n = int(input("Enter a number: "))
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print("Reverse number:", rev)
reverse_number()


# ============================================================
# 2. NUMBER PALINDROME
# ============================================================

# 1. With arguments, with return value
def number_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return original == rev
print("Palindrome:", number_palindrome(121))

# 2. With arguments, without return value
def number_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    if original == rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
number_palindrome(121)

# 3. Without arguments, with return value
def number_palindrome():
    n = int(input("Enter a number: "))
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return original == rev
print("Palindrome:", number_palindrome())

# 4. Without arguments, without return value
def number_palindrome():
    n = int(input("Enter a number: "))
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    if original == rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")
number_palindrome()


# ============================================================
# 3. ARMSTRONG NUMBER
# ============================================================

# 1. With arguments, with return value
def armstrong(n):
    original = n
    power = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10
    return total == original
print("Armstrong:", armstrong(153))

# 2. With arguments, without return value
def armstrong(n):
    original = n
    power = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10
    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
armstrong(153)

# 3. Without arguments, with return value
def armstrong():
    n = int(input("Enter a number: "))
    original = n
    power = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10
    return total == original
print("Armstrong:", armstrong())

# 4. Without arguments, without return value
def armstrong():
    n = int(input("Enter a number: "))
    original = n
    power = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10
    if total == original:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
armstrong()


# ============================================================
# 4. REVERSE A STRING
# ============================================================

# 1. With arguments, with return value
def reverse_string(s):
    return s[::-1]
print("Reversed string:", reverse_string("Python"))

# 2. With arguments, without return value
def reverse_string(s):
    print("Reversed string:", s[::-1])
reverse_string("Python")

# 3. Without arguments, with return value
def reverse_string():
    s = input("Enter a string: ")
    return s[::-1]
print("Reversed string:", reverse_string())

# 4. Without arguments, without return value
def reverse_string():
    s = input("Enter a string: ")
    print("Reversed string:", s[::-1])
reverse_string()


# ============================================================
# 5. STRING PALINDROME
# ============================================================

# 1. With arguments, with return value
def string_palindrome(s):
    return s == s[::-1]
print("Palindrome:", string_palindrome("madam"))

# 2. With arguments, without return value
def string_palindrome(s):
    if s == s[::-1]:
        print("Palindrome string")
    else:
        print("Not a palindrome string")
string_palindrome("madam")

# 3. Without arguments, with return value
def string_palindrome():
    s = input("Enter a string: ")
    return s == s[::-1]
print("Palindrome:", string_palindrome())

# 4. Without arguments, without return value
def string_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print("Palindrome string")
    else:
        print("Not a palindrome string")
string_palindrome()


# ============================================================
# 6. FACTORIAL
# ============================================================

# 1. With arguments, with return value
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial:", factorial(5))

# 2. With arguments, without return value
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial:", fact)
factorial(5)

# 3. Without arguments, with return value
def factorial():
    n = int(input("Enter a non-negative number: "))
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial:", factorial())

# 4. Without arguments, without return value
def factorial():
    n = int(input("Enter a non-negative number: "))
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial:", fact)
factorial()


# ============================================================
# 7. PRIME NUMBER
# ============================================================

# 1. With arguments, with return value
def prime_number(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Prime:", prime_number(7))

# 2. With arguments, without return value
def prime_number(n):
    if n < 2:
        print("Not a prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            return
    print("Prime number")
prime_number(7)

# 3. Without arguments, with return value
def prime_number():
    n = int(input("Enter a number: "))
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Prime:", prime_number())

# 4. Without arguments, without return value
def prime_number():
    n = int(input("Enter a number: "))
    if n < 2:
        print("Not a prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            return
    print("Prime number")
prime_number()


# ============================================================
# 8. SUM OF DIGITS
# ============================================================

# 1. With arguments, with return value
def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print("Sum of digits:", sum_digits(1234))

# 2. With arguments, without return value
def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    print("Sum of digits:", total)
sum_digits(1234)

# 3. Without arguments, with return value
def sum_digits():
    n = int(input("Enter a number: "))
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print("Sum of digits:", sum_digits())

# 4. Without arguments, without return value
def sum_digits():
    n = int(input("Enter a number: "))
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    print("Sum of digits:", total)
sum_digits()


# ============================================================
# 9. LARGEST OF THREE NUMBERS
# ============================================================

# 1. With arguments, with return value
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Largest number:", largest(10, 25, 15))

# 2. With arguments, without return value
def largest(a, b, c):
    if a >= b and a >= c:
        print("Largest number:", a)
    elif b >= a and b >= c:
        print("Largest number:", b)
    else:
        print("Largest number:", c)
largest(10, 25, 15)

# 3. Without arguments, with return value
def largest():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Largest number:", largest())

# 4. Without arguments, without return value
def largest():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a >= b and a >= c:
        print("Largest number:", a)
    elif b >= a and b >= c:
        print("Largest number:", b)
    else:
        print("Largest number:", c)
largest()


# ============================================================
# 10. FIBONACCI SERIES
# ============================================================

# 1. With arguments, with return value
def fibonacci(n):
    a = 0
    b = 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print("Fibonacci series:", fibonacci(7))

# 2. With arguments, without return value
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
fibonacci(7)

# 3. Without arguments, with return value
def fibonacci():
    n = int(input("How many terms? "))
    a = 0
    b = 1
    series = []
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print("Fibonacci series:", fibonacci())

# 4. Without arguments, without return value
def fibonacci():
    n = int(input("How many terms? "))
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
fibonacci()
