student={
    "name":"Aayush",
    "score":{
        "maths":98,
        "phy":97,
        "chem":95
    }
}
print(student["name"])
print(student["score"]["maths"])
print(len(student))

# We can typecast data into different forms.

print(list(student.keys()))