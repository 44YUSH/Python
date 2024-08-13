# Find sum of 1+2+3+...+n.

# While Loop :
n = int(input("Enter the number : "))
i=1
sum1=0
while i <= n:
    sum1+=i
    i+=1
print("Using WHILE loop : ",sum1)

# For Loop : 
sum2=0
for j in range(1, n+1):
    sum2+=j
print("Using  FOR  loop : ",sum2)