
# 1. Print the length of "Python"
s = "Python"
print(len(s))  


# 2. Print the first and last characters of "Programming"
s = "Programming"
print(s[0])   
print(s[10])  


# 3. Find the output
s = "Computer"
print(s[2])   
print(s[5])   
print(len(s)) 


# 4. Print the first three characters of "Education"
s = "Education"
print(s[0])
print(s[1])
print(s[2])



# 5. Find the output
s = "Hello World"
print(s[-1])  
print(s[-3])  
print(len(s)) 


# 6. Second character from beginning and end
s = "Developer"
print(s[1])  
print(s[-2]) 


# 7. Find the output
s = "Python Programming"
print(s[7])  
print(s[-7])  
print(len(s)) 


# 8. Print the middle character of "Python"
s = "Python"
mid = len(s) // 2
print(s[mid]) 


# 9. Find the output
s = "Kiran Academy"
print(s[5])  
print(s[-5])  
print(s[0])   
print(s[-1])  


# 10. Accept a string and print length, first and last characters
s = input("Enter a string: ")
print("Length:", len(s))
if len(s) > 0:
    print("First character:", s[0])
    print("Last character:", s[-1])
else:
    print("The string is empty.")


# 11. Find the output
s = "Artificial Intelligence"
print(len(s))  
print(s[10])   
print(s[-10])  

# 12. Third character from beginning and end
s = "Information"
print(s[2])   
print(s[-3])  


# 13. Find the output
s = "123456789"
print(s[4])          
print(s[-4])         
print(s[len(s) - 1]) 
print(s[-len(s)])    


# 14. Accept a string and print length and selected characters
s = input("Enter a string: ")
print("Length:", len(s))
if len(s) >= 2:
    print("First character:", s[0])
    print("Last character:", s[-1])
    print("Second character:", s[1])
    print("Second-last character:", s[-2])
elif len(s) == 1:
    print("First character:", s[0])
    print("Last character:", s[-1])
    print("Second and second-last characters are unavailable.")
else:
    print("The string is empty.")


# 15. Find the output
s = "Programming"
print(len(s)) 
print(s[10])   
print(s[-11])  
