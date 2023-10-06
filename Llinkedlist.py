class linkedlist:
    def __init__(self,data):
        self.next=None
        self.data=data
def InsertNode(root,key):
    if root==None:
        root=linkedlist(key)
        return root
    else:
        temp=root
        while temp.next!=None:
            temp=temp.next
        temp.next=linkedlist(key)
        
        return temp
def display(root):
    if root==None:
        print('none')
    else:
        temp=root
        while temp!=None:
            print(temp.data,'->',end=" ")
            temp=temp.next
            return temp
root=None
root=linkedlist(1)
root=InsertNode(root,2)
display(root)
print()
root=InsertNode(root,3)
root=InsertNode(root,5)
root=InsertNode(root,3)
root=InsertNode(root,2)
root=InsertNode(root,1)
display(root)