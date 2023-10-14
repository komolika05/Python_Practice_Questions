#Write a program to calculate a factorial of a number

f = int(input("Enter the number "))
s=1
i=1
while i<=f:
    s=s*i
    i +=1
    
print(s)