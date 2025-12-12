numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for n in numbers:
    if n > 0:
        total += n

print("Sum of positive numbers: ",total)