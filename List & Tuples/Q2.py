l = []
n = int(input("Enter the size of LIST : "))
print("Enter the elements : ")
for i in range (0,n):
    ele=input()
    l.append(ele)
print("Your LIST is : ", l)

m = l.copy()
m.reverse()

if(l==m):
    print("YES, It's a pelindrome no.")
else:
    print("NO, It's NOT a pelindrome no.")