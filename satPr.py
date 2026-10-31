# num = int(input("Enter a number"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# -------------------------------
# num = 0
# if num == 0:
#     print("Zero")
# elif num < 0:
#     print("Negative")
# else:
#     print("Positive")

# -------------------------------

# a = 12345
# rev = 0
# ans = 0
# while a > 0:
#     digit = a % 10
#     ans = ans * 10 + digit
#     a = a//10
# print(ans)

# -------------------------------

# a= 12345
# rev = ""

# for chr in str(a):
#     rev = chr+rev
# num = int(rev)
# print(num)
    
    

# -------------------------------

# a = 1223
# rev = ""

# for chr in str(a):
#     rev = chr+rev
# num = int(rev)

# if num == a:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# -------------------------------

# num =6
# count = 0


# for i in range(1,num+1):
#     if num % i == 0:
#         count += 1
    
# if count == 2:
#    print("Prime")
# else:
#     print("Not prime")

# -------------------------------

# for i in range(2,101):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# -------------------------------

# num = 4
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)

# -------------------------------
# num = 3
# sqr = num **2
# print(sqr)
# cube = num **3
# print(cube)

# -------------------------------

# l1 = [1,2,3,4,6,7,8,9,10]

# for i in l1:
#     if i%2 == 0:
#         print(i)

# ----------------------------
# l1 = [1,2,3,4,6,7,8,9,10]
# count  = 0

# for i in l1:
#     if i%2 == 0:
#         count+=1
# print(count)

# ----------------------------------
# l1 = [1,2,3,4,5,6,7,8]
# rev = l1[::-1]
# print(rev)    
# l1.reverse()
# print(l1) 

# ----------------------------------

# arr = [2,3,4,5,6]

# for num in arr:
#     if num > 1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#                 print(num,end=" ")
        
        
# ----------------------------------

# l1 = ["str","pr",1,2,3]

# for i in l1:
#     if isinstance(i,str):
#         print(i)

# ------------------------------------

# l1 = ["str","pr",1,2,3]

# for i in l1:
#     if isinstance(i,int):
#         print(i)

# ------------------------------------

# l1 = (1,2,3,4)
# p = list(l1)

# print(max(p))

# # ---------------------------------------

# l1 = (1,2,3,4)
# p = list(l1)

# print(min(p))

#---------------------------------------

# l1 = (1,2,3,4,5)
# p = list(l1)
# print(sum(p))

#---------------------------------------

# l1 = (1,2,3,4,5,6,7,8)
# count = 0

# for i in l1:
#     count+=1
# print(count)

#---------------------------------------

# l1 = (1,2,3,4,5,6,7,8)
# count = 0
# i = 0
# while i < len(l1):
#     count += l1[i] 
#     i+=1
# print(count)

#---------------------------------------

# l1 =(1,2,3,4,5,6,7,8)
# p = list(l1)
# for i in p:
#     if i % 2 == 0:
#         print(i)

#---------------------------------------

# l1 = {"name":"Harshal","age":21}

# for keys,values in l1.items():
#     print(keys,":",values)

#---------------------------------------

# marks = {"Math":81,"Science":21,"C":89}
# total = 0
# for values in marks.values():
#     total = total + values
    
# print(total)

#---------------------------------------

# st1 = {"A":85,"B":91,"C":21,"D":46}
# for i in st1.values():
#     if(i > 60):
#         print(i)

#---------------------------------------

# st1 = {"A":85,"B":91,"C":21,"D":46}
# count = 0
# for i in st1.values():
#     if i > 35:
#         count+=1
# print(count)

#---------------------------------------

st1 = {"A":85,"B":91,"C":21,"D":46}
maxx = 0

for keys,values in st1.items():
    if values > maxx:
        maxx = values
print(keys,":",maxx)
    





    