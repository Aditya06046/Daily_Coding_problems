class linkedlist:
    def __init__(self,data):
        self.next=None
        self.data=data
def InsertNode(root,key):
    if root==None:
        root=linkedlist(key)
    else:
        temp=root
        while temp.next!=None:
            temp=temp.next
        temp.next=linkedlist(key)
def display(root):
    if root==None:
        print('none')
    else:
        temp=root
        while temp!=None:
            print(temp.data,'->',end=' ')
            temp=temp.next
def length_of_loop(root1):
    temp=root1
    l=[]
    while temp!=None:
        if temp in l:
            break
        l.append(temp)
        temp=temp.next
    print(temp.data)
            
        
    
    
def linkedlist_palindrome(root):
    l=[]
    while root!=None:
        l.append(root.data)
        root=root.next
    print(l)
    if l==l[::-1]:
        print(True)
    else:
        print(False)
# def Bigoo(root):
#     temp=root
#     while temp!=None and temp.next!=None:
def getLength(root):
    temp=root
    cnt=0
    while temp!=None:
        temp=temp.next
        cnt+=1
    return cnt
def creating_loop(root,root1):
    x=getLength(root)
    y=getLength(root1)
    print(x,y)
    temp=root
    temp2=root1
    while temp2.next!=None:
        temp2=temp2.next
    cnt=1
    val=root
    while temp.next!=None:
        temp=temp.next
        cnt+=1
        if cnt==3:
            val=temp
    temp2.next=val
    temp.next=root
    
root=linkedlist(1)
InsertNode(root,2)
InsertNode(root,3)
InsertNode(root,5)
InsertNode(root,6)
InsertNode(root,7)
InsertNode(root,8)
#-----------------
root1=linkedlist(12)
InsertNode(root1,18)
InsertNode(root1,28)
#display(root1)
creating_loop(root,root1)
#display(root1)
#linkedlist_palindrome(root)
length_of_loop(root1)
