def array_diff(a,b):
    arrOfDiff=[]
    for e in a:
        if e not in b:
            arrOfDiff.append(e)
    
    return arrOfDiff

print(array_diff([1,2,2],[1]))