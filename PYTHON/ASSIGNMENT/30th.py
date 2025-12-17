s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

indices = []

for i in range(len(s1) - len(s2) + 1):
    if s1[i:i+len(s2)] == s2:
        indices.append(i)

if indices:
    print("Indices:", indices)
else:
    print(-1)
