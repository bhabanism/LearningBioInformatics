import sys # you must import "sys" to read from STDIN

file = open("dataset_2_7.txt")
lines = file.read().splitlines()
txt = lines[0]
pattern = lines[1]
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
    

    
"""for i in (len(lines)):
    print('Line ' + str(i+1) + ' is ' + str(len(lines[i])) + ' characters long.')"""
    

"""lines = sys.stdin.read().splitlines() # read in the input from STDIN

for i in xrange(len(lines)):
    print('Line ' + str(i+1) + ' is ' + str(len(lines[i])) + ' characters long.')"""
