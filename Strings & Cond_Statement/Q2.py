#Q2) i.
num = int(input("Enter a number : "))
result = num % 2
if(result == 0):
    print("EVEN")
else:
    print("ODD")
print()

#Q2) ii.
a=int(input("Enter the 1st no. : "))
b=int(input("Enter the 2nd no. : "))
c=int(input("Enter the 3rd no. : "))

if(a>=b and b>=c):
    print(a, " is the GREATEST no.")
elif(b>=c):
    print(b, " is the GREATEST no.")
else:
    print(c, " is the GREATEST no.")
print()

#Q2) iii.
n=int(input("Enter a no. to check if its a mult of 7 : "))
ans=n%7
if(ans==0):
    print("YES")
else:
    print("NO")