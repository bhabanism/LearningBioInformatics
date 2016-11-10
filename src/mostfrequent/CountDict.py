# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

# Copy your PatternCount function from Replication.py into the line below.
def PatternCount(Pattern, Text):
    count = 0 # output variable
    status = 0
    patternLen = len(Pattern)
    for i in range((len(Text))):
        status = Text.find(Pattern,i,i+patternLen)
        if(status>-1):
            count = count + 1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(CountDict(lines[1],int(lines[0])))
