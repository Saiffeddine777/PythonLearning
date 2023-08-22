#Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
#The first word within the output should be capitalized only if the original word was capitalized 
#(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    if text=="":
        return ""
    arr= list(text)
    i=0
    while i<len(arr):
        if arr[i] == "_" or arr[i] == "-":
            arr[i+1] = arr[i+1].upper()
            arr.pop(i)
        else:
            i+=1
        
    return "".join(arr)

print(to_camel_case("the_stealth_warrior"))