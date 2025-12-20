s = input("Enter a string: ")

print("\nMenu")
print("1. Find frequency of a character")
print("2. Replace a character with another character")
print("3. Remove first occurrence of a character")
print("4. Remove all occurrences of a character")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    ch = input("Enter character to find frequency: ")
    print("Frequency of", ch, "is:", s.count(ch))

elif choice == 2:
    old = input("Enter character to replace: ")
    new = input("Enter new character: ")
    print("Modified string:", s.replace(old, new))

elif choice == 3:
    ch = input("Enter character to remove (first occurrence): ")
    print("Modified string:", s.replace(ch, "", 1))

elif choice == 4:
    ch = input("Enter character to remove (all occurrences): ")
    print("Modified string:", s.replace(ch, ""))

else:
    print("Invalid choice")
