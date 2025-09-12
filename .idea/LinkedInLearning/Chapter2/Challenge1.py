def factorial(num):
    # Your code goes here.
    if isinstance(num, int) and num >= 0:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    else:
        return None

number = 5
result = factorial(number)
print(result)