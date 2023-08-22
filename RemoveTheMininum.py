def remove_smallest(numbers):
    copy = list(numbers)
    if len(numbers) == 0:
         return []
    smallest=copy[0]
    for e in copy:
         if e<smallest:
              smallest = e
    
    copy.pop(copy.index(smallest))
    return copy

print(remove_smallest([5, 3, 2, 1, 4]))