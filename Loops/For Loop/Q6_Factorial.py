# Find the FACTORIAL of first n nums.

n = int(input("Enter the num : "))

# FOR loop : 
Factorial=1

for i in range(1, n+1):
    Factorial *= i
print("Using  FOR  loop : ",Factorial)

# WHILE loop :
j=1
factorial=1
while j<=n:
    factorial *= j
print("Using WHILE loop : ",factorial)