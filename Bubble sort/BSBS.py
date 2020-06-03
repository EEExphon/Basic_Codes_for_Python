def bubblesort (sample):

    stop = len(sample) - 1
    swap = True
    
    while swap == True :
        
        swap = False
        
        for i in range (stop):
            
            if sample [i] > sample [i+1]:
                sample [i], sample [i+1] = sample [i+1], sample [i]
                swap = True
                
    return sample

List = [234212,231,4,32,4,2134,21,43,2,52,43,213,4,3214,12,34,2134,213,4,3214,2341]

NewList = bubblesort(List)

print(NewList)
                     
