# Print the squre of numbers from 1 to 10.
list=[]
i = 1
while i<=10:
    sq=i*i
    list.append(sq)
    i+=1
print(list)

tup=()
tup=list.copy()
print(tup())
search = int(input("Enter the no. to search in the list : "))