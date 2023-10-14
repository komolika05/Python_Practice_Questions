#Write a program to identify prime numbers

is_prime = True
x= int(input("Enter Number "))
i=2
while i<x:
    if x%i==0 :
        is_prime = False
        break
    i +=1

if is_prime == True :
    print("It is a prime number")

else :
    print("It is not a prime number!")