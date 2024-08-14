# WAF to print element of a list in single line.

l = ["a","b","c"]
m = [1,2,3,4,5,6]
def Single (list):
    for i in list:
        print(i, end=" ")
    print()

    
Single(l)
Single(m)