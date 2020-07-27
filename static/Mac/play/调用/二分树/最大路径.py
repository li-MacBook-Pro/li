#定义一个二叉路径类，包括当前节点、左节点和右节点
class PathSummation():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#定义一个函数，返回根节点最后的停值和不停值较大那个
def maxPathSum(root):
    print(max(helper(root)))

#定义一个辅助函数，递归算出根节点停值和不停值
def helper(root):
    if root == None:
        return [0, 0]
    #得到左子节点的停值与不停值
    leftG, leftS = helper(root.left)
    #得到左子节点的停值与不停值
    rightG, rightS = helper(root.right)
    #不停值
    Go = max(root.value + leftG, root.value +rightG, root.value)
    #停值
    Stop = max(leftS, rightS, leftG, rightG, root.value+leftG+rightG)
    return Go, Stop

node1 = PathSummation(1)
node2 = PathSummation(2)
node3 = PathSummation(-2)
node4 = PathSummation(10)
node5 = PathSummation(12)
node6 = PathSummation(2)
node7 = PathSummation(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
maxPathSum(node1)
