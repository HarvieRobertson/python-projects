#Starting at part B
age = int(input("How old are you: "))
height = int(input("How tall are you(cm): "))
if (age < 12):
    print("You are too young for this ride. ")
elif (age >= 12):
    print("You are old enough for this ride.")
    if (height < 140):
        print ("But you are not tall enough")
    else:
     print("Have a good time!")


#B2
num = int(input("Please enter an integer: "))
if (num > 0):
    print("Positive number.")
else:
    print("Negative number.")
if (num % 2 == 0):
    print("Even number.")
else :
    print("Odd Number")
if ((num > 100) | (num < -100)):
    print("Number is large.")
else: 
    print("Number is not big.")


correct_username = "student"
correct_password = "python123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username:
    print("Username recognised")

if username == correct_username and password == correct_password:
    print("Login successful!")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Access granted")
    else:
        print("You must be at least 18.")
else:
    print("Incorrect username or password.")


amount = float(input("Enter shopping total: "))

if amount >= 100:
    discount = amount * 0.20
elif amount >= 50:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print(f"Original amount: £{amount}")
print(f"Discount: £{discount}")
print(f"Final amount: £{final_amount}")


first_number = float(input("Enter the first number: "))
operator = input("Enter an operator: ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    if second_number == 0:
        print("Cannot divide by zero")
    else:
        print(first_number / second_number)
elif operator == "%":
    print(first_number % second_number)
elif operator == ">":
    print(first_number > second_number)
elif operator == ">=":
    print(first_number >= second_number)
elif operator == "<":
    print(first_number < second_number)
elif operator == "<=":
    print(first_number <= second_number)
else:
    print("Invalid operator")
