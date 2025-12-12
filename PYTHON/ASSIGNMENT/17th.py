numbers = list(map(int, input("Enter numbers separated by space: ").split()))

most_frequent = None
max_count = 0

for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        most_frequent = num

print("Most frequent element : ", most_frequent)
print("Total frequent is : ", max_count)
