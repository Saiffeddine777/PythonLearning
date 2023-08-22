def maskify(cc):
    chars = list(cc)
    i = -1
    string=""
    
    while i>= -len(chars):
        if i<-4:
            chars[i]="#"
        i=i-1
    
    return string.join(chars)

print(maskify("4556364607935616"))