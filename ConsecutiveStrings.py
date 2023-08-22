def longest_consec(strarr,k):
    if k>len(strarr) or len(strarr)==0 or k<=0 :
        return ""
    
    if k==1:
        longest = strarr[0]
        for e in strarr:
            if len(e)>len(longest):
                longest = e
        return longest
    

    arrOfLengths = []
    for i in range(len(strarr)-k+1):
        item ="".join(strarr[i:i+k])
        arrOfLengths.append(item)
        

    longest = arrOfLengths[0]
    
    for e in arrOfLengths:
        if len(e)>len(longest):
            longest = e
    
    return longest

print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))

    

        

