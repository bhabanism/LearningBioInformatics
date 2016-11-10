# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = ""
    for i in range(len(Pattern)-1, -1,-1) :
        c = Pattern[i]
        if c == "A" :
            revComp += "T"
        elif c == "T" :
            revComp += "A"
        elif c == "C" :
            revComp += "G"
        elif c == "G" :
            revComp += "C"
    return revComp


# Copy your reverse function from the previous step here.


# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = ""
    for i in range(0, len(Nucleotide)) :
        c = Nucleotide[i]
        if c == "A" :
            comp += "T"
        elif c == "T" :
            comp += "A"
        elif c == "C" :
            comp += "G"
        elif c == "G" :
            comp += "C"
    return comp



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ReverseComplement("AAAACCCGGT"))
