#reverse numeber
a = int(input("Enter number -->"))

rev = 0
while(a > 0):
    rem = a % 10
    rev = rev * 10 + rem
    a = a//10
    
print("Reverse number is -->",rev)
