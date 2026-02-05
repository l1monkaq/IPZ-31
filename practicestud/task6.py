def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = 3
result = factorial(number)
print(f"Result: {result}")