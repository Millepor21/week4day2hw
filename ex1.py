words = ['this' , 'is', 'a', 'sentence', '.']

def reverse(alist):
    
    for i, astring in enumerate(alist):
        astring = astring[::-1]
        alist[i] = astring
    alist = alist[::-1]
    return alist

reverse(words)