import re
text="This is my first Program"
patterns=['kavin','Program']
for pattern in patterns:
    print ('Looking for "%s" in "%s" ->'%(pattern,text))
    if re.search(pattern,text,re.I):
        print('found a match')
    else:
        print("no match")
    
