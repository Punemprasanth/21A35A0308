
# series
val = int(input("Enter the number:"))
x=0
y=0
for i in range(1,val+1):
        if(i%2!=0):
           x=x+7
        else:  
           y=y+6
if(val%2!=0):
    print('{}term in accordance to the program is {}'. format(val,x-7))
else:
    print('{}term in accordance to the program is {}'. format(val,y-6))



text='india'
index=0
for i in text:
    print("text[",index,"",1)
    index +=1

text='india is great'
print(text.title())

text='India is Great'
print(text.swapcase())

text='India is Great'
print(text.split())

# join case
str='India','is','Great'
print('-'.join(str))

strl='donkey'
print (list(enumerate(strl)))

strl='donkey monkey'
print (list(enumerate(strl)))

strl='88'
print(strl.zfill(4))

strl='jai balayya'
print(strl.upper())

strl='jai balayya'
print(strl.lower())

# slicing program
strl='indian'
print(strl[::])

import string
print(string.digits)
print(string.ascii_letters)
chr='g'
print('a'<=chr<='z')


strl='hello'
print(dir(strl))


import re
strl="she sells sea shells at sea shore"
pl="sells"
if re.match(pl,strl):
       print("match found")
else:
       print(pl,"not prasent in the string")


import re
strl="she sells sea shells at sea shore"
pl="sells"
if re.match(pl,strl):
       print("match found")
else:
       print(pl,"not prasent in the string")

import re
strl="she sells sea shells at sea shore"
p1="sea"
rep="ocean"
ns=re.sub(p1,rep,strl,1)
print(ns)

import re
p=r"(aeiou)"
if re.search(p,"clue"):
    print("mathcy vowel")




n = int(input('enter the number :'))

a=0

b=0

for i in range(1,n+1):
   if(i%2!=0):
     a= a+2
else:
    b= b+1
if(n!=0):
    print('{}'.format(a-2))
else:
    print('{}'.format(b-1))




































