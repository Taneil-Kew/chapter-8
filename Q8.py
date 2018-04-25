#question 8
def reverse(word):
    new = ""
    for i in range(len(word)):
        new += word[len(word)-i-1]
    return print(new)

def mirror(word):
    return word + reverse(word)


mirror("woo")
