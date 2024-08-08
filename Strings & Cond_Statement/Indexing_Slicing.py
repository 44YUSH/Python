#   0   1   2   3   4   5   6   7   8   9   10   11     forward
#   R   a   d   h   a   _   K   r   i   s    h    n
#  -12 -11 -10 -9  -8  -7  -6  -5  -4  -3   -2   -1     backward                 

str = "Radha Krishn"
chr=str[0]
print(chr)

print(str[6])

# Slicing
print(str[ :5])                    #str[0:5]
print(str[6:len(str)])             #str[6:12]
print(str[0:5]+"  "+str[6:12])

print(str[-5:-1])
print(str[-11:-7])



