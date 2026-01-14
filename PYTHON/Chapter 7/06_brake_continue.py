for i in range(5):
    if i == 3:
        break  # Exit tje loop right now
    print(i, end=",")


for i in range(6):
    if i == 5:
        continue  # Skip this iteration
    print(i)