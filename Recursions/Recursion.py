# When a function calls itself repeatedly.     |       |
                                        #      +-------+
def show(n):                            #      |   1   |
    if(n==0):                           #      +-------+
        return                          #      |   2   |
    print(n)                            #      +-------+
    show(n-1)                           #      |   3   |
                                        #      +-------+
                                        #       L I F O
show(3)                   