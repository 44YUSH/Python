data={
    "Name":"Aayush",
    "Score":{
        "maths":98,
        "phy":97,
        "chem":95
    }
}

# data.keys()
print(data.keys())
print(len(data))
print(list(data.keys()))

# data.values()
print(data.values())
print(list(data.values()))

# data.items()
print(data.items())

pairs=list(data.items())
print(pairs[1])

# data.get("key") ---> It's IMPORTANT because in normal
#                      case if there is an error the codes
#                      which are appearing after the errors
#                      will also NOT work.

print(data.get("Score"))

