#Print All Perfect Squares Between 1 and N
n = int(input())
for i in range(1, n + 1):
    if i * i <= n:
        print(i * i, end=" ")   
        