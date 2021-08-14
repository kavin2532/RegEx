import re
s="this was test"
pat="w[abc]s"
result=re.findall(pat,s)
print(result)
if result:
    print("true")
pat="\w+@.\w+.(com|edu)"
s="abc@gmail.com"
res=re.match(pat,s)
print(res)
s="this is test"
pat="t[^abc]st"
res=re.findall (pat,s)
print(res)
pat="this was test"
pat="t.i"
res=re.findall (pat,s)
print(res)
s="fooaaabcde"
pat="a*"
res=re.findall(pat,s)
print(res)
pat="a*b"
res=re.findall (pat,s)
print(res)
pat="a+b"
res=re.findall (pat,s)
print(res)
res=re.findall ("a+",s)
print(res)
s="fooaaaooob"
res=re.findall ("o{2,3}",s)
print(res)
res=re.findall ("o{3,4}",s)
print(res)
res=re.search ("a*b",s)
print(res)
print(res.group ())
print(res.span())
s="fooaaabcde"
res=re.search ("a*b",s)
print(res)
print(res.group())
print(res.start ())
print(res.end())
print(res.span ())
res=re.sub("(blue|red|green)","black","This is red shoes and blue socks")
print(res)
res=re.split("\W","This is test")
print(res)
res=re.findall ("\d+","12 cats,14 dogs and 9 cows")
print(res)
res=re.findall ("$t?^t","this is test")
print(res)
res=re.findall ("$t","this is test")
print(res)
res=re.findall ("^t","this is test")
print(res)
res=re.findall ("^t?$t","this is test")
print(res)
res=re.findall("^t.\w+$t","this is test")
print(res)
res=re.findall("^t.\w+$t","this is test")
print(res)
