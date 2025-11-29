name = input ("Enter Your name : ")
letter = '''Dear {name},
        You are selected!
        <|Date|>'''
# print(letter.replace(f"<|Name|>","{name}").replace(f"<|Date|>","01 dec 2025") )
print(letter.replace("<|Date|>","01 dec 2025") ) 