#-*- coding: utf-8 -*-
print('～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～')
# 人家说的：实际上就是广度优先遍历, 借助一个队列（这里用数组代替）就可以实现:
# 1、先将root节点加入队列
# 2、队列不为空时取队列首节点
# 3、打印节点的值，然后将该节点的左、右子节点先后加入队尾（核心步骤，广度优先体现在这）
# 4、回到2，直到队列为空

#先序 ：上左右  中序：左中右  后续：左右中
class A:
    def __init__(self,value,left=None,right=None):
        self.value= value
        self.left= left
        self.right= right

g=A(7)
f=A(6)
e=A(5)
d=A(4)
c=A(3,f,g)
b=A(2,d,e)
a=A(1,b,c)

def func(a):
    if a != None:
        print(a.value)
        func(a.left)
        func(a.rigth)

func(a)
    # if (a.left != None):
    #     func(a.left)
    # if (a.right != None):
print('～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～')
#定义一个二叉树类，包括当前节点、左节点和右节点
class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#先序遍历：先遍历根，再遍历左子树，最后遍历右子树
def DLR(root):
    if root == None:
        return
    print(root.value)
    DLR(root.left)
    DLR(root.right)

#中序遍历：先遍历左子树，再遍历根，最后遍历右子树
def LDR(root):
    if root == None:
        return
    LDR(root.left)
    print(root.value)
    LDR(root.right)

#后序遍历：先遍历左子树，再遍历右子树，最后遍历根
def LRD(root):
    if root == None:
        return
    LRD(root.left)
    LRD(root.right)
    print(root.value)

node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
DLR(node1)
print()
LDR(node1)
print()
LRD(node1)


print('～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～～')
#funb(number)numbre层阶梯:一层加上二层爬
def funb(n):
    if n==1:
        return 1
    elif  n==2:
        return 2
    else :
        return funb(n-1)+funb(n-2)

print(funb(5))
print(funb(6))
print(funb(7))
print(funb(8))
print(funb(9))
print(funb(10))