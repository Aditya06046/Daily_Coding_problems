import math
s='aditya'
key=1324
val=str(key)
temp=''
j=0
for i in s:
    temp+=str(ord(i)+int(val[j])-96)+','
    
    j+=1
    if j==int(math.log(key,10)+1):
        j=0
    
print(temp[:-1])