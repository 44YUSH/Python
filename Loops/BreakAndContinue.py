# Print all ODD no. from 1 to 10.
print("ODD")
i=1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i+=1
print()

# Print all the EVEN no. from 1 to 10.
print("EVEN")
i=1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i+=1