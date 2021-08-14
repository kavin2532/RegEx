import re
num="\w{5}\d{4}[A-Z]"
pan="INQPK2517F"
s=re.match(num,pan)
print(s)
if s:
    print("its is pan number")
else:
    print("not a pan number")
