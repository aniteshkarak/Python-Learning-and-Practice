numbers = list(map(int, input("Enter numbers separated by space: ").split()))

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        break

if is_sorted:
    print("The list is sorted in ascending order")
else:
    print("The list is NOT sorted in ascending order")
