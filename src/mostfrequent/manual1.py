import sys # you must import "sys" to read from STDIN


txt = "GATCCAGATCCCCATAC"
pattern = "AC"
print(txt)
print("pattern - {}".format(pattern))
patternLen = len(pattern)
print(patternLen)
print(len(txt))

count = 0
for i in range((len(txt))):
    status = txt.find(pattern,i,i+patternLen)
    if(status>-1):
        count = count + 1

print("count - {}".format(count))
    
