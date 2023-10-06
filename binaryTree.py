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
    if not temp:
        return 0
    else:
        q=[]
        q.append(temp)
        parent=None
        while(len(q)):
            val=q[0]
            q.pop(0)
            if val.data==key:
                return 1
            if val.left!=None:
                q.append(val.left)
            if val.right!=None:
                q.append(val.right)
            
        return 0
# def deleteNode(temp,key):
#     q=[]
#     l={}
#     q.append(temp)
#     l.append(temp.data)
#     parent=None
#     while(len(q)):
#         val=q[0]
#         q.pop(0)
#         if val.left!=None:
#             q.append(val.left)
#             l[val.right]=val.right.data
#         if val.right!=None:
#             q.append(val.right)
#             l[val.right]=val.right.data
#             
#     
#         
#     return l
#
l1=[]
l2=[]
l3=[]
# Three traversal orders in a single function
def Trds(root):
    if root!=None:
        l1.append(root.data)
        Trds(root.left)
        l2.append(root.data)
        Trds(root.right)
        l3.append(root.data)
root=TreeDemo(1)
root.left=TreeDemo(3)
root.right=TreeDemo(2)
root.left.left=TreeDemo(4)
root.left.right=TreeDemo(5)
#print(Display(root))
Trds(root)
print(l1,l2,l3)
#     print(SearchNode(root,4))
#print(deleteNode(root,2))