t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# a) Print contents in two separate halves
mid = len(t1) // 2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# b) Create a tuple of even values
t2 = tuple(x for x in t1 if x % 2 == 0)
print("Even values tuple:", t2)

# c) Concatenate another tuple with t1
t3 = (11, 13, 15)
concatenated_tuple = t1 + t3
print("Concatenated tuple:", concatenated_tuple)

# d) Find maximum and minimum values
maximum = max(t1)
minimum = min(t1)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
