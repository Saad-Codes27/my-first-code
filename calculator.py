print("=== My calculator ===")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("addition:", first_number + second_number)
print("subtraction:", first_number - second_number)
print("multiplication:", first_number * second_number)

if second_number == 0:
    print("division: cannot divide by zero")
else:
    print("division:", first_number / second_number)
