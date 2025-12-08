a = (1,6, 61 , 61 ,32, 132, 5366) 

print(a)

no = a.count(61)
print(no)

i = a.index(132)
print(i)

# tuple are immutable.
# Tuples cannot be changed after creation → immutable

# len((1, 2, 3))    3  length tuple
# max((2, 5, 1))    5  maximum tuple
# min((2, 5, 1))    1  minimum 
# sum((5, 5, 10))    20  Sum of all this number
# sorted((3, 1, 2))    [1, 2, 3]  Sorted
# tuple([1, 2, 3])    (1, 2, 3)  Convert tuple
