def longest(a1, a2):
    acc = []
    for e in a1:
        if acc.count(e)==0:
            acc.append(e)

    for e in a2:
        if acc.count(e)==0:
            acc.append(e)
    
    acc.sort()
    
    return "".join(acc)

print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
