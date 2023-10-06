x=342
s=''
# # # # # # cnt=0
# # # # # # while x!=0:
# # # # # #     y=x%10
# # # # # #     x=x//10
# # # # # #     s+=str(int(y)*(10**cnt))+'+'
# # # # # #     cnt+=1
# # # # # # s=s[:-1]
# # # # # # print(s)
t=str(x)
cnt=len(t)-1
for i in t:
    s+=str(int(i)*(10**cnt))+'+'
    cnt-=1
print(s[:-1])