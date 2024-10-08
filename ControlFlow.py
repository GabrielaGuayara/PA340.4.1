# 1. Declares 1 variable x, and then assigns 7 to it. Print out “Less than 10” if x is less than 10
x = 7
if x < 10 :
    print("Less than 10")

#Changing x to 15
x = 15

#2. If-else statement that prints out “Less than 10” if x is less than 10, and “Greater than 10” if x is
#greater than 10
x = 7
if x < 10 :
    print("Less than 10")
else:
    print("Greater than 10")

x = 15

#3. if...elif...else statement
x = 15
if x < 10 :
    print("Less than 10")
elif x >10  and x < 20 :
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")

x = 50

#T4.  if-else statement that prints “Out of range” if the number is less than 10 or greater than 20 and
# prints “In range” if the number is between 10 and 20 
x = 15
if x < 10 or x > 20 :
    print("Out of range")
else:
    print("In range")

x = 5


#5.  if...elif...else statements to print out grades A, B, C, D, F
score = int(input("Please enter your score: "))
if score < 0 or score > 100:
    print("Score out of range")
elif 90 <= score <= 100:
    print("A")
elif 80 <= score < 90 :
    print("B")
elif 70 <= score < 80 :
    print("C") 
elif 60 <= score < 70 :
    print("D")
else: 
    print("F")
    
#6. Program to display how much tax the user would have to pay according to status and income

status = input("Please enter your status('Single', 'Married'): ")
income = int(input("Please enter your income: "))
taxesToPay = 0


if(status) == "Single" :
    if 0 <= income <= 8350 :
        taxesToPay = 0.10 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 8351<= income <= 33950 :
        taxesToPay = 0.15 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 33951<= income <= 82250 :
        taxesToPay = 0.25 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

    elif 82251<= income <= 171550 :
        taxesToPay = 0.28 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 171551<= income <= 372950 :
        taxesToPay = 0.33 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    else:
        taxesToPay = 0.35 * income 
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

elif(status) == "Married Filing Jointly" :
    if 0 <= income <= 16700 :
        taxesToPay = 0.10 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 16701<= income <= 67900 :
        taxesToPay = 0.15 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 67901<= income <= 137050 :
        taxesToPay = 0.25 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

    elif 137051<= income <= 208850 :
        taxesToPay = 0.28 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 208851<= income <= 372950 :
        taxesToPay = 0.33 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    else:
        taxesToPay = 0.35 * income 
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

elif(status) == "Married Filing Separately" :
    if 0 <= income <= 8350 :
        taxesToPay = 0.10 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 8351<= income <= 33950 :
        taxesToPay = 0.15 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

    elif 33951<= income <= 68525 :
        taxesToPay = 0.25 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

    elif 68526<= income <= 104425 :
        taxesToPay = 0.28 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 104426<= income <= 186475 :
        taxesToPay = 0.33 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    else:
        taxesToPay = 0.35 * income 
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

elif(status) == "Head of Household":
    if 0 <= income <= 11950 :
        taxesToPay = 0.10 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 11951<= income <= 45500 :
        taxesToPay = 0.15 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

    elif 45501<= income <= 117450 :
        taxesToPay = 0.25 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")

    elif 117451<= income <= 190200 :
        taxesToPay = 0.28 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    
    elif 190201<= income <= 372950 :
        taxesToPay = 0.33 * income
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
    else:
        taxesToPay = 0.35 * income 
        print(f"You have to pay {round(taxesToPay, 2)} in taxes")
else:
    print("Invalid entry")