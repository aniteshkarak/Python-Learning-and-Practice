def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n * n) 
    return result


nums = list(map(int, input("Enter numbers separated by space: ").split()))

print("Squares:", square_list(nums))
