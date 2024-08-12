tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the no. to find in tuple :"))
i=0
while i < len(tup):
    if(tup[i]==x):
        print("Found at IDX : ", i)
    i += 1