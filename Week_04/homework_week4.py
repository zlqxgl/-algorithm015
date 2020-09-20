#860柠檬水找零
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5,c10 = 0, 0
        for b in bills:
            if b == 5:
                c5 += 1
            elif b == 10:
                c5 -= 1
                if c5 < 0:
                    return False
                c10 += 1
            else:
                if c10 > 0:
                    c10 -= 1
                    c5 -= 1
                    if c5 < 0:
                        return False
                else:
                    c5 -= 3
                    if c5 < 0:
                        return False
        return True
#122买卖股票最佳时机
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
#455分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == [] or s == []:return 0
        g.sort()
        g.reverse()
        s.sort()
        s.reverse()
        i,j,count = 0,0,0
        while i != len(g) and j != len(s):
            if g[i] <= s[j]:
                j += 1
                count += 1
            i += 1
        return count
#874模拟行走机器人
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = {'up': [0, 1, 'left', 'right'],
                     'down': [0, -1, 'right', 'left'],
                     'left': [-1, 0, 'down', 'up'],
                     'right': [1, 0, 'up', 'down']}
        x, y,res = 0, 0, 0
        dir = 'up'
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command > 0:  # 正数的话进行模型行进操作
                for step in range(command):
                    if (x + direction[dir][0], y + direction[dir][1]) not in obstacles:
                        x += direction[dir][0]
                        y += direction[dir][1]
                        res = max(res, x ** 2 + y ** 2)
                    else:break
            else:  # 负数的话只改变行进方向
                if command == -1:  # 右转
                    dir = direction[dir][3]
                else:  # 即command == -2，左转
                    dir = direction[dir][2]
        return res
#127单词接龙
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        n= len(beginWord)
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                dic[word[:i] + "*" + word[i+1:]].append(word)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            cur, level = queue.pop(0)
            for i in range(n):
                temp = cur[:i] + "*" + cur[i+1:]
                for word in dic[temp]:
                    if word == endWord:return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                dic[temp] = []
        return 0
#200岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = collections.deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"
        return num_islands
#529扫雷游戏
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a, b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
        elif board[a][b] == 'E':
            d = [*itertools.product((-1, 0, 1), repeat=2)]
            q, v, m, n = [(a, b)], {(a, b)}, len(board), len(board[0])
            while q:
                p = []
                for i, j in q:
                    c, t = 0, []
                    for di, dj in d:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n:
                            c += board[x][y] == 'M'
                            (x, y) not in v and t.append((x, y))
                    board[i][j] = c and str(c) or p.extend(t) or v.update(t) or 'B'
                q = p
        return board
#55跳跃游戏
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
#33搜索旋转排序数组
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        left,right =0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:right = mid - 1
                else:left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:left = mid + 1
                else:right = mid - 1
        return -1
#240搜索二维矩阵
class Solution:
    def searchMatrix(self, matrix, target):
        m,n=len(matrix),len(matrix[0])
        if m==0 or n==0:return False
        i, j = m-1, 0
        while i>=0 and j<n:
            if target >matrix[i][j]:j+=1
            elif target<matrix[i][i]:i-=1
            else:return True
        return False
#153寻找旋转排序数组中最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:#中间值比右边界大，最小值在中间值的右边，挪动左边界
                left=mid+1
            elif nums[mid]<nums[right]:#中间值比右边界值小，最小值在中间值左边，挪动右边界
                right=mid
        return nums[left]



