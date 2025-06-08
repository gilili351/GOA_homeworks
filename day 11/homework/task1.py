# Task 1
n = int(input("Enter a number n: "))
for i in range(0, n + 2):
    print(i)

# Task 2
age = int(input("Enter your age: "))
has_card = input("Do you have a student card? (yes/no): ").strip().lower()

if age < 18 or has_card == "yes":
    print("You have a discount!")
elif age >= 60 and has_card != "yes":
    print("You get a senior discount!")
else:
    print("No discount applicable.")

# Task 3
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > 0 and b > 0:
    print("Both numbers are positive")
elif (a > 0 and b <= 0) or (b > 0 and a <= 0):
    print("Only one number is positive")
else:
    print("Neither number is positive")

# Task 4
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    print("Result:", x + y)
elif operation == "-":
    print("Result:", x - y)
elif operation == "*":
    print("Result:", x * y)
elif operation == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Invalid operation!")
else:
    print("Invalid operation!")

# Task 5
print("Task 5: Please upload or describe the image for analysis.")