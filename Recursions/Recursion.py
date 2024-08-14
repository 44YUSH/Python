# When a function calls itself repeatedly.     |       |
                                        #      +-------+
def show(n):                            #      |   1   |  ----\   /-->  3
    if(n==0):                           #      +-------+       \ /
        return                          #      |   2   |  ------X---->  2
    print(n)                            #      +-------+       / \
    show(n-1)                           #      |   3   |  ----/   \-->  1
                                        #      +-------+  
                                        #       L I F O
show(3)                   