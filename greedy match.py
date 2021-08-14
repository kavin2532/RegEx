import re
s='<html><head><title></title>'
len(s)
print(re.match('<.*>',s).span()) #length of the values 0,27
print(re.match('<.*>',s).group())   #print all value
