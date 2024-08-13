# Find sum of 1+2+3+...+n.

n = int(input("Enter the number : "))
i=1
sum=0
while i <= n:
    sum+=i
    i+=1
print(sum)