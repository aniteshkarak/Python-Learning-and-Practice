n = int(input("enter a number : "))

print("*"*n)
for i in range(2,n):
    print("*", end="")
    print(" "*(n-2), end="")
    print("*")

print("*"*n)