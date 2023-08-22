def dont_give_me_five(start,end):
    if start<end:
        arr = []    
        while start<=end:
            if  '5' not in str(start):
                arr.append(start)
            
            start = start + 1
        return len(arr)
           

print(dont_give_me_five(101, 159))