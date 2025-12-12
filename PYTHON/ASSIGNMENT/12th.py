def intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result

a = list(map(int, input("Enter first list elements: ").split()))
b = list(map(int, input("Enter second list elements: ").split()))

print("Common elements:", intersection(a, b))
