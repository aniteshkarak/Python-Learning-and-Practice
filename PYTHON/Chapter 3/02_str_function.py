name = "Anitesh karak"

print(len(name))

# Changing case & formatting
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())

# Searching & finding substrings
print(name.find("oyhg"))  #returns the lowest index where substring sub is found, or –1 if not found.
print(name.index("ka"))
print(name.startswith("Ani")) #return true or false
print(name.endswith("k")) #return true or false

# Modifying / Transforming
print(name.replace("Anitesh","Raja"))
print(name.strip())  #returns a new string with leading and trailing characters (defaults to whitespace) removed.
print(name.split(","))  #splits string into a list of substrings, using sep as delimiter (default whitespace).
print(name.join(["My name is "," and my son father name is ",", thanks"])  # → "2025-11-11"
)
# .
# .
# .
# .
# .
# .
# .
# .
# .

# and many more string function available, please kindly ask chtgpt for more string function
