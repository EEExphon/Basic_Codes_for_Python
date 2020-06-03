def Sort(x,y):
    
    X = len(x)
    Y = len(y)
    
    if X >= Y:
        R = X
    else:
        R = Y

    N = X + Y
    
    SortedList = []
    
    xi = 0
    yi = 0
    LEN = 0
    m = 0
    n = 0
    
    while LEN != N-1:

        if xi == X:
            for bnm in range (Y-yi-1):
                SortedList.append(y[yi+bnm+1])
                LEN = LEN + 1
        elif yi == Y:
            for bnm in range (X-xi-1):
                SortedList.append(x[xi+bnm+1])
                LEN = LEN + 1
        else:
        
            if x[xi] > y[yi]:
                SortedList.append(y[yi])
                yi = yi + 1
                LEN = LEN + 1

            elif x[xi] == y[yi]:
                SortedList.append(x[xi])
                SortedList.append(y[yi])
                xi = xi + 1
                yi = yi + 1
                LEN = LEN + 2

            elif x[xi] < y[yi]:
                SortedList.append(x[xi])
                xi = xi + 1
                LEN = LEN + 1
    
    return SortedList
            
            
L = [1,2,3,4,5]
T = [2,2,2,2,2,2,2]

LIST = Sort(L,T)

print(LIST)
