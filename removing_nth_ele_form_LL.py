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
            print(temp.data,'->')
            temp=temp.next
def Removing_nth_ele(root,key):
    temp=root
    cnt=0
    while temp!=None:
        cnt+=1
        temp=temp.next
#    print(cnt)
    temp=root
    cnt1=0
    while temp.next!=None:
        if cnt1==cnt-key-1:
            break
        cnt1+=1
        temp=temp.next
    temp.next=temp.next.next
#     print(temp.data,'...')
#     print(cnt1,'???')
root=linkedlist(1)
InsertNode(root,2)
InsertNode(root,3)
InsertNode(root,4)
InsertNode(root,5)
InsertNode(root,6)
InsertNode(root,7)
InsertNode(root,8)
display(root)
key=5
Removing_nth_ele(root,key)
print(',,,,,,,,,,,,,,,,,,')
display(root)