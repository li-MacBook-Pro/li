#定义一个最大面积类，包括两个函数
class MaxArea(object):
    def maxAreaOfIsland(self, grid):
    	#存储最大岛屿面积
        self.maxArea = 0
        #地图行数
        row = len(grid)
        #地图列数
        col = len(grid[0])
        #从上到下，从左到右遍历地图
        for i in range(row):
            for j in range(col):
            	#若发现陆地
                if grid[i][j] == 1:
                    current = 1
                    #进入测算函数
                    self.dfs(i, j, current, grid)
        print(self.maxArea)

    def dfs(self, k, z, current, grid):
    	#初始点设为2
        grid[k][z] = 2
        #向上走若不越界，则更新当前点和面积
        if k > 0 and grid[k-1][z] == 1:
            current = self.dfs(k-1, z, current+1, grid)
        #向下走若不越界，则更新当前点和面积
        if k < (len(grid)-1) and grid[k+1][z] ==1:
            current = self.dfs(k+1, z, current+1, grid)
        #向左走若不越界，则更新当前点和面积
        if z > 0 and grid[k][z-1] == 1:
            current = self.dfs(k, z-1 ,current+1, grid)
        #向右走若不越界，则更新当前点和面积
        if z < (len(grid[0])-1) and grid[k][z+1] == 1:
            current = self.dfs(k ,z+1, current+1, grid)
        #取当前岛屿和历史岛屿较大那个
        self.maxArea = max(self.maxArea, current)
        return current

m = MaxArea()
m.maxAreaOfIsland([[0,0,0,0,1,1,0],
                   [0,1,1,0,1,1,0],
                   [0,1,1,0,0,0,0],
                   [0,0,1,0,0,1,1],
                   [0,0,0,0,0,0,0],
                   [0,0,1,1,0,0,0],
                   [0,0,0,1,0,0,1]])
