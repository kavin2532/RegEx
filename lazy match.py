import re
s='<html><head><title>Title<\title>'
len(s)
32
print(re.match('<.*>',s).span())
(0,32)
print(re.match('<.*?>',s).group())