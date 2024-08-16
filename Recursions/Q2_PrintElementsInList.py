# Write a recursive function to print all elements in a list.
# { HINT : Use LIST & INDEX as parameters. }

def PrintElement(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    PrintElement(list, idx+1)

alphabets=["a","b","c","d"]
PrintElement(alphabets)