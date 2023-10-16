#Write a program of a working calulator performing all the operations and restart

import os

while True: 
    os.system('cls' if os.name == 'nt' else 'clear')

    x = input("Enter First Number : ")
    operator = input("Choose an operator (+, -, *, /, %) ")
    y = input("Enter Second Number : ")

    if operator == "+":
        print ("Your answer is ", int(x) + int(y))

    elif operator == "-":
        print ("Your answer is ", int(x) - int(y))

    elif operator == "*":
        print ("Your Answer is ", int(x) * int(y))

    elif operator == "/":
        print ("Your Answer is ", int(x) / int(y))

    elif operator == "%":
        print ("Your answer is ", int(x) % int(y))

    else:
        print ("Invalid Operation")

    again = input("Do you want to use calculate again? Yes/No ")

    if again == "no" :
        break
