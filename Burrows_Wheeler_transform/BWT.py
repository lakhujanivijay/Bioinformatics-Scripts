
#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

s='Tomorrow_and_tomorrow_and_tomorrow$'
s=list(s)
final=[]
for i in range(0,len(s)):
   s.append(s[0])
   del(s[0])
   str1 = ''.join(s)
   final.append(str1)

final.sort()

bwt=''.join(map(lambda x: x[-1], final))

print bwt
