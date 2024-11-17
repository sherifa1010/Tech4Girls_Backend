#Division calculator
try:
    numerator = int(input("Enter the numerator:"))
    denominator = int(input("Enter the denominator:"))
    if denominator == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = numerator / denominator
        print("the result is:", result)
except ValueError:
    print("Error: please enter valid integers.")