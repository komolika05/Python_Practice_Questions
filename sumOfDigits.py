#Write a program to calculate the sum of all digits of a number

number = int(input("Write a Number "))

x_str = str(number)

x_array = [int(digit) for digit in x_str]

sum = 0

for digit in x_array :
    sum += int(digit)

print(sum)

