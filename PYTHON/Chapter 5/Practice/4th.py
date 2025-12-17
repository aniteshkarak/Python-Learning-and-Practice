s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')

print(s)  # in python 1==1.0 (its true)
print(len(s))