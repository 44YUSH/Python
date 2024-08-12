# a = str(input("Enter 1st subject : "))
# x = int(input("Enter marks of 1st subject : "))
# b = str(input("Enter 2nd subject : "))
# y = int(input("Enter marks of 2nd subject : "))
# c = str(input("Enter 3rd subject : "))
# z = int(input("Enter marks of 3rd subject : "))
# result={
#     a : x,
#     b : y,
#     c : z
# }
# print(result)

result = {}
print(result)

a=input("Enter 1st subject : ")
x=input("Enter MARKS of 1st sub : ")
SUBJECT1={a : x}
result.update(SUBJECT1)
print(result)

b = str(input("Enter 2nd subject : "))
y = int(input("Enter marks of 2nd subject : "))
SUBJECT2={b : y}
result.update(SUBJECT2)
print(result)

c = str(input("Enter 3rd subject : "))
z = int(input("Enter marks of 3rd subject : "))
SUBJECT3={c : z}
print(SUBJECT3)