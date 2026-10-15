# Python Fundamentals - code examples from the 30 theory questions

# Q6: variables and objects
x = 10
y = x
print(x is y)                      # True (same object)

# Q7: id()
a, b = 100, 100
print(id(a) == id(b))              # True (small ints are cached)
p, q = [1], [1]
print(id(p) == id(q))              # False

# Q8: type()
print(type(10), type(3.14), type("hi"), type([1, 2]))

# Q9-10: input() returns str, so convert it
# n = int(input("Enter a number: "))
print("5" + "3")                    # 53 (string concatenation)
print(int("5") + int("3"))         # 8

# Q11: basic data types
print(25, 3.14, 2 + 3j, "Python", True)

# Q12: float precision
print(0.1 + 0.2)                   # 0.30000000000000004

# Q13: complex numbers
z = 3 + 4j
print(z.real, z.imag)              # 3.0 4.0

# Q15-16: type casting
print(int("25"), str(100), float(5))   # explicit
print(5 + 2.5)                         # implicit -> 7.5

# Q17-19: operators
print(5 + 3, 5 > 2, 5 > 2 and 3 < 1)

# Q20: == vs is
m = [1, 2]
n = [1, 2]
print(m == n, m is n)              # True False

# Q22: string immutability
s = "Python"
try:
    s[0] = "J"
except TypeError as e:
    print("Error:", e)
s = "J" + s[1:]
print(s)                           # Jython

# Q23: indexing
t = "PYTHON"
print(t[0], t[-1])                 # P N

# Q24-25: slicing
print(t[1:4], t[::2], t[::-1])     # YTH PTO NOHTYP
print(repr(t[4:1]), repr(t[1:4:-1]), t[4:1:-1])   # '' '' OHT

# Q26: print() with sep and end
print("a", "b", "c", sep="-")
print("Hello", end=" ")
print("World")

# Q29: mutable vs immutable
lst = [1, 2]
lst[0] = 9
print(lst)
tup = (1, 2)
try:
    tup[0] = 9
except TypeError as e:
    print("Error:", e)

# Q30: inspecting a program
val = 5 + 2.0
print(val, type(val), id(val))