def complement(text) :
    comp = ""
    for i in range(0, len(text)) :
        c = text[i]
        if c == "a" :
            comp += "t"
        elif c == "t" :
            comp += "a"
        elif c == "c" :
            comp += "g"
        elif c == "g" :
            comp += "c"
    return comp


text= "atcg"
print(complement(text))

""" for reverse ?
for i in range(len(text)-1, -1,-1) : """
