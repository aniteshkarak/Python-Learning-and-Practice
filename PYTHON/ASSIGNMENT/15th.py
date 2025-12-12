list1 = list(map(int, input("Enter first list numbers: ").split()))
list2 = list(map(int, input("Enter second list numbers: ").split()))

common = []

for x in list1:
    if x in list2:
        common.append(x)

print("Common elements:", common)
