#Write a program to identify a leap year

year =int(input("Enter Year "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Yes, It is a leap Year")

else :
    print("No, It is not a leap year")
    
