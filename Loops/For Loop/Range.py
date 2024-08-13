# Range function returns a sequence of number.
# Range( start? , stop , step?)    ---> '?' is optional.
# It starts from 0 and increase by 1 by default, and stops before a specified number.

for i in range(10):             # (? , 10 , ?)
    print(i)

print("-----")

for j in range(4 , 10):         # (4 , 10 , ?)
    print(j)

print("-----")

for k in range(2 , 10 , 2):     #(2 , 10 , 2)   ---> EVEN
    print(k)

print("-----")

for l in range(1 , 10 , 2):     #(2 , 10 , 2)   ---> ODD
    print(l)