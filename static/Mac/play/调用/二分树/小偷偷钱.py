#定义一个二叉房子类，包括当前节点、左节点和右节点
class House():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#定义一个函数，返回根节点最后的偷值和不偷值较大那个
def rob(root):
    a = helper(root)
    print(max(a[0], a[1]))

#定义一个辅助函数，递归算出根节点偷值和不偷值
def helper(root):
    if(root == None):
        return [0, 0]
    left = helper(root.left)
    right = helper(root.right)
    #当前节点偷值等于当前节点的偷值加上左右子节点的不偷值
    robValue = root.value + left[1] + right[1]
    #当前节点不偷值等于左右子节点的偷值与不偷值中较大的那个值
    skipValue = max(left[0], left[1]) + max(right[0], right[1])
    #返回偷值和不偷值
    return [robValue, skipValue]

node1 = House(3)
node2 = House(4)
node3 = House(5)
node4 = House(1)
node5 = House(3)
node7 = House(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node7
DLR(node1)
rob(node1)
