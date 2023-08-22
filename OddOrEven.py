def odd_or_even(arr):
    sum= 0
    for e in arr:
        sum +=e

    if sum%2==1:
        return "odd"
    else:
        return "even"
    
print(odd_or_even([0, 1, 3]))