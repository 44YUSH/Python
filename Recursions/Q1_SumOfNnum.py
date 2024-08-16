# Write a recursive function to calculate the sum of first n natural numbers.
# 1 + 2 + 3 + ... + n

def TotalSum(n):
    if(n == 1):
        return 1
    else:
        return n + TotalSum(n-1)
    
print(TotalSum(4))