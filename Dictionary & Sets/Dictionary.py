dict = {
    "name" : "Aayush",
    "cgpa" : 9.7,
    "marks" : [97, 98, 95],
    "is_adult": True,
    300404 : "DOB"
}
print(dict["name"], dict["marks"])

# DICTIONARIES are mutable so, we can change the values.
dict["name"]="Aayush_Sith"
dict[1234]="Adding new number"
print(dict)