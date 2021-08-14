import re
string ="Python java c++ perl shell ruby tcl c c#"
print(re.findall (r"\bc[\W+]*",string,re.M|re.I))
print(re.findall (r"\bp[\w]*",string,re.M|re.I))
print(re.findall (r"\bs[\w]*",string,re.M|re.I))
print(re.sub (r'\W+',"",string)) #combie all the words form group
it=(re.finditer(r"\bc[(\W\s)]*",string))
for match in it:
    print("'{g}'was found between the indices{s}".format(g=match.group(),s=match.span()))
    
/4[poiuytr12
