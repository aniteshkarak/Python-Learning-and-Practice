p1= "Make a lot of money"
p2= "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter a sentence : ")

# comment = comment.lower()

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print("This message is a SPAM message")

else:
    print("This is not a spam message")