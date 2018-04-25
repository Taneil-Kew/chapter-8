#question 4
def count_letters(strng,ch,start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(count_letters("banana", "a", 2) == 3)
