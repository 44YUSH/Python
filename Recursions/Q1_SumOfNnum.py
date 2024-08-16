# Write a recursive function to calculate the sum of first n natural numbers.
# 1 + 2 + 3 + ... + n

def TotalSum(n):
    if(n <= 0):
        return "It's NOT a Natural Number."
    elif(n == 1):
        return 1
    else:
        return n + TotalSum(n-1)
    
print(TotalSum(10))