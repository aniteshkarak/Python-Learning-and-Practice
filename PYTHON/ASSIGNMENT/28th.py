try:
    numbers = list(map(int, input("Enter integers separated by space: ").split()))

    if len(numbers) != len(set(numbers)):
        raise ValueError("Duplicate numbers found in the list")

    print("List accepted. No duplicates found.")

except ValueError as e:
    print("Error:", e)
