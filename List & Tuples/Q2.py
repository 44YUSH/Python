l = []
n = int(input("Enter the size of LIST : "))
print("Enter the elements : ")
for i in range (0,n):
    ele=int(input())
    l.append(ele)
print("Your LIST is : "l)

m = l.copy()
m.reverse()
print(m)

if(l==m):
    print("YES, Its a pelindrome no.")
else:
    print("NO, Its NOT a pelindrome no.")