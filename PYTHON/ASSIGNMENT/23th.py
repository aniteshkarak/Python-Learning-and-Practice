def remove_key(data, key):
    if key in data:
        del data[key]  
    else:
        print("Key not found")
    return data


dict = {"name": "Ankit", "age": 20, "city": "KGP"}

remove = input("Enter key to remove: ")

updated = remove_key(dict, remove)
print("Updated dictionary:", updated)