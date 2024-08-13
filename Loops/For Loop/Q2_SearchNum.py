# Search for a number X in this tuple using loop.
tup=(1,4,9,16,25,36,49,64,81,100)
X = int(input("Enter the number to SEARCH in the tuple : "))
idx=0
for el in tup:
    if(el==X):
        print("Found at idx : ", idx)
    idx += 1