# class access:
#     def __init__(self):
#         self.name='aditya'
#         self.__val=3
#         self._tom='tom'
#     def display():
#         print(self.name)
#         print(self.__val)
#         print(self._tom)
# var=access()
# #print(dir(var))
# print(var.val)
# s='asdhfas'
# for i in s:
#     if i=='f':
#         pass
#     else:
#         print(i)
# print('----')
# for i in s:
#     if i=='f':
#         continue
#     else:
#         print(i)
def docString():
    # multiplication 
    '''this is me not you like me'''
    return 2*3
print(docString.__doc__)