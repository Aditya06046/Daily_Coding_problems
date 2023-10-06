import binaryTree
class Bst:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def Inorder(root):
    if root!=None:
        Inorder(root.left)
        print(root.data,end=' ')
        Inorder(root.right)
def InsertNode(root,key):
    if root==None:
         root=Bst(key)
    else:
        if key<root.data:
            if root.left==None:
                root.left=Bst(key)
            else:
                InsertNode(root.left,key)
        if key>=root.data:
            if root.right==None:
                root.right=Bst(key)
            else:
                InsertNode(root.right,key)
#def searchNode(root,key):
    
def deleteNode(root,key):
    if root==None:
        print('Not possible')
        return
    else:
        if binaryTree.SearchNode(root,key):
            print('Yes')
        else:
            print('noo')
        

root=Bst(5)
InsertNode(root, 2)
InsertNode(root, 3)
InsertNode(root, 1)
InsertNode(root, 4)
InsertNode(root, 3)
InsertNode(root, 8)
InsertNode(root, 7)
Inorder(root)
deleteNode(root,4)