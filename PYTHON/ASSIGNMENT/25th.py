n = int(input("Enter the value of n: "))

total = 0 

for i in range(1, n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i

print("Sum of the series is:", total) 
