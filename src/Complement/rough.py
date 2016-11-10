

def reverse(text) :
    for i in range(len(text)-1, -1,-1) : 
        print(text[i], end="")

text= "abcd"
reverse(text)
