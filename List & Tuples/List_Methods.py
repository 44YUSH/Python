list=[2, 1, 3]

list.append(4)
print(list)                # OUTPUT: [2, 1, 3, 4]

list.sort()
print(list)                # OUTPUT: [1, 2, 3, 4]

list.sort(reverse=True)
print(list)                # OUTPUT: [4, 3, 2, 1]

list.reverse()
print(list)                # OUTPUT: [1, 2, 3, 4]

list.insert(1, 3)
print(list)                # OUTPUT: [1, 3, 2, 3, 4]

list.remove(3)
print(list)                # OUTPUT: [1, 2, 3, 4]

list.pop(3)
print(list)                # OUTPUT: [1, 2, 3]