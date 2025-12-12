n = int(input("Enter a number: "))

positive = abs(n)
total = 0

while positive > 0:
    total += positive % 10 
    positive = positive // 10   

print("Sum of digits:", total)
