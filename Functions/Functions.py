# Functions are group of statements that performs a specific task.
# We use FUNCTIONs in code to avoid writing of same codes again and again.
# We use it to reduce REDUNDENCY. 


# defination func_name (parameter? a , parameter? b):
#            algorithms
#            return? value
# func_name (argument a , argument b)  ---> Function call


# Example 1 : 
x = int(input("Enter 1st num : "))
y = int(input("Enter 2nd num : "))

def calcSum(a, b):
    result = a + b
    print("Sum of both num is : ",result)
    return result
calcSum(x, y)

print("-------------------------")

# Example 2 : Here, in this fun, neither there is INPUT nor RETURN.
# Hence, they are OPTIONAL '?'.
def p():
    print("Radhe Radhe")
p()
p()
p()