# Lists
l = []
 
# Adding Element into list
l.append(5)
l.append(10)
print("Adding 5 and 10 in list", l)
 
# Popping Elements from list
l.pop()
print("Popped one element from list", l)
print()

# Tuple
t = tuple(l)
 
# Tuples are immutable
print("Tuple", t)
print()

# Dictionary
d = {}
 
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)
 
# Removing key-value pair
del d[10]
print("Dictionary", d)
