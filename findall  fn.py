import re
line='python Orientation course helps professionals fish best opportunities py '
print("find all words starts with p")
print (re.findall (r"\bp[\w]*",line))# \b match boundaries outside
print("find all five characters long words")
print (re.findall(r"\b\w{5}",line)) # its print all the first five word in the value
print (re.findall(r"\b\w{5}\b",line)) # its print only accurate 5 letters  in the words
print ("find all 4,6 char long words")
print (re.findall(r"\b\w{4,6}\b",line))
print ("find all 14 char long words")
print (re.findall(r"\b\w{13,}\b",line))

