# if-elif-else
#    
#    if(condition):
#         Statement 1
#    elif(condition):
#         Statement 2
#    else(condition):
#         Statement N

age=int(input("Enter your age : "))

if(age>=18):
    print("Can VOTE")
elif(age<18 and age>0):
    print("Not Capable")
else:
    print("ERROR")
