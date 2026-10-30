#Print the Fibonacci Series for N Terms
n = int(input())
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b