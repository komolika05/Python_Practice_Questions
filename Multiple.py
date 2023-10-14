#Write a program to calculate the multiples of a number in a particular range of numbers

x = input("Starting range ")
i = int(x)
a = input("range = ")
b = input("Multiple of ")
while i < int(a):
    i +=1 
    if i%int(b)==0:
        print(i)
    