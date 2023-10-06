class TreeDemo:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def Display(temp):
    if temp==None:
        return 
    Display(temp.left)
    print(temp.data,end=' ')
    Display(temp.right)
def insertNode(temp,data):
    if not temp:
        temp=TreeDemo(data)
    l=[]
    l.append(temp)
    while(len(l)):
        val=l[0]
        l.pop(0)
        if val.left==None:
            val.left=TreeDemo(data)
            break
        else:
            l.append(val.left)
        if val.right==None:
            val.right=TreeDemo(data)
            break
        else:
            l.append(val.right)
def SearchNode(temp,key):
#     if temp-==None:
#         return 'false'
#     if temp.data==key:
#         print('found')
#     return SearchNode(temp.left,key)
#     return SearchNode(temp.right,key)
    if not temp:
        return 0
    else:
        q=[]
        q.append(temp)
        while(len(q)):
            val=q[0]
            q.pop(0)
            if val.data==key:
                return 'found'
            if val.left!=None:
                q.append(val.left)
            if val.right!=None:
                q.append(val.right)
        return 'not found'
root=TreeDemo(1)
root.left=TreeDemo(3)
root.right=TreeDemo(2)
root.left.left=TreeDemo(4)
root.left.right=TreeDemo(5)
print(Display(root))
print(Display(root))
print(SearchNode(root,4))
