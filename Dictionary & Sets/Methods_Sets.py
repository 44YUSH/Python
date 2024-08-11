s = set()

# set.add(el) adds an element
s.add("Krishn")
s.add(2)
s.add("Radha")
s.add(3)
s.add(7)

print(s)

# set.remove(el) deletes an element
s1=s.copy()

s1.remove(3)
s1.remove("Krishn")
print(s1)