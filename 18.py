#Calculate the Power of a Number Without Using the Exponentiation Operator
base = int(input())
exponent = int(input())
result = 1

for _ in range(exponent):
    result *= base

print(result)