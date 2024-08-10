# t=tuple(input("Enter your tuple : "))
# print(t)
# print(t.count('a'))

# print(t)
# l=[]
# l.append(t)
# print(l)
# l.sort()
# print(l)

l = []
n = int(input("Enter the size of LIST : "))
print("Enter the elements : ")
for i in range (0,n):
    ele=input()
    l.append(ele)
print("Your LIST is : ", l)

l.sort()
print(l)