# WAF to find the factorial of N.

n = int(input("Enter the num : "))

def fact(N):
    factorial=1
    for i in range(1, N+1):
        factorial*=i
    print(factorial)

fact(n)