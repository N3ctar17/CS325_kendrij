def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example: Calculate the factorial of 5
result = factorial(5)
print(f"The factorial of 5 is: {result}")

user_input = input("Enter a non-negative integer to calculate its factorial: ")

try:
    number = int(user_input)
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        # Calculate factorial
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")