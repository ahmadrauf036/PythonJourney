# Error handling

a=int(input("Enter Dividend: "))
b=int(input("Enter Divisor: "))

try:
    print(a/b)
except ZeroDivisionError:
    print("Division by zero not possible.")
