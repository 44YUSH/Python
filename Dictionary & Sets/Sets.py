# Duplicate values are ignored in sets.
# Here, SETs are MUTABLE but the ELEMENTS of the SETs are IMMUTABLE.

sets = {1, 2, 2, 2, 3, "Aayush", "Krishn", 5}

print(sets)
print(type(sets))

MTset=set() # is the syntax for empty set.