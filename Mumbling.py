def accum(s):
    arr = list(s)
    count = 0
    result = []
    string="-"
    for e in arr:
        chunk = e.upper()+(count*e.lower())
        result.append(chunk)
        count = count+1
    return string.join(result)

print (accum("ZpglnRxqenU"))