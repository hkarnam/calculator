ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

print("=== Welcome to your Interactive Python calculator ===")

a = int(input("Please enter the first value: "))
b = int(input("Please enter the second value: "))

print("Great! Now enter the operation.")
print("These are the available operations: ")

print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer division")
print("6 - Modulo")

operation = int(input("--> Enter the corresponding Integer: "))

if operation == ADDITION:
    result = a + b
    print(f" The addition of {a} + {b} is: {result}")

elif operation == SUBTRACTION:
    result = a - b
    print(f" The subtraction of {a} - {b} is: {result}")

elif operation == MULTIPLICATION:
    result = a * b
    print(f" The multiplication of {a} * {b} is: {result}")

elif operation == DIVISION:
    if b == 0:
        print(" Division by 0. Please enter other value of b")
    else:
        result = a / b
        print(f" The division of {a} / {b} is: {result}")

elif operation == INTEGER_DIVISION:
    if b == 0:
        print(" Division by 0. Please enter other value of b")
    else:
        result = a // b
        print(f" The Integer division of {a} // {b} is: {result}")

elif operation == MODULO:
    result = a % b
    print(f" The modulo of {a} % {b} is {result}")

else:
    print("please choose a valid operation")