s1='mynameisherobolthehero'
s2='heromynameisherobolthe'
def right_rotate(s1,s2):
    i=s1.count(s2[0])
    l=[]
    l=list(i for i in range(len(s1)) if s1[i]==s2[0])
    print(l)
    for x in l:
        s3=''
        y=s1[:x]
        s3=s1[x:]+y
        print(x,s3)
        if s3==s2:
            return 1
    return -1
print(right_rotate(s1,s2))