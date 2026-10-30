#Check Whether a Given Number Is a Perfect Number
n = int(input())
divisors_sum = 0

for i in range(1, n):
    if n % i == 0:
        divisors_sum += i

if divisors_sum == n:
    print("Yes")
else:
    print("No")