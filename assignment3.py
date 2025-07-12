#Calculate Factorial Using a Function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

number = 5
print("The factorial of", number, "is", factorial(number))


import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

print("Square root:", square_root)
print("Natural log (ln):", natural_log)
print("Sine (in radians):", sine_value)
