thisList =  ["banana","kiwi","apple"]
newList=[]

forTheWhile=[]
forForRange=[]

for element in thisList:
    new =element.upper()
    newList.append(new)

print(newList)

i=0

while i<len(thisList):
    new = thisList[i].upper()
    forTheWhile.append(new)
    i=i+1

print(forTheWhile)

for i in range(len(thisList)):
    new = thisList[i].upper()
    forForRange.append(new) 

print()