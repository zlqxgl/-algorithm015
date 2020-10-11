#64最小路径和
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]
#91解码方法
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[i+1] += dp[i]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i+1] += dp[i-1]
        return dp[-1]
#221最大正方形
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        maxSquare = maxSide * maxSide
        return maxSquare
#647回文子串
class Solution:
    def countSubstrings(self, s: str) -> int:
        if s == '':
            return 0
        end = s[-1]
        num = 0
        for i in range(len(s)):
            if s[i] == end and s[i:] == s[i:][::-1]:
                num += 1
        return self.countSubstrings(s[:-1])+num
#32最长有效括号
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """ 动态规划dp """
        n = len(s)
        dp, res = [0]*n, 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i - 2 > 0 else 0) + 2
                else:
                    j = i - dp[i-1] - 1
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i-1] + (dp[j-1] if j-1>=0 else 0) + 2
                res = max(res, dp[i])
        return res
#72编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] ) + 1
        #print(dp)
        return dp[-1][-1]
#363矩形区域不超过K的最大数值和
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            total = [0] * m
            for right in range(left, n):
                for i in range(m):
                    total[i] += matrix[i][right]
                pre = [0]
                p = 0
                for row in total:
                    p += row
                    loc = bisect.bisect_left(pre, p - k)
                    if loc != len(pre):
                        res = max(p - pre[loc], res)
                    bisect.insort(pre, p)
        return res
#410分割数组的最大值
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        def test_mid(mid):
            num = 1
            s = 0
            for i in nums:
                if s+i > mid:
                    s = i
                    num += 1
                else:
                    s += i
            return num > m
        while left < right:
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:left = mid+1
            else:right = mid
        return left
#76最小覆盖子串
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        cnt = collections.Counter(t)
        ans = ''
        n = 0 
        l = 0
        for r, ch in enumerate(s):
            if ch not in cnt: 
                continue
            cnt[ch] -= 1
            if cnt[ch] == 0:
                n += 1
            while s[l] not in cnt or cnt[s[l]] < 0:
                if s[l] in cnt: cnt[s[l]] += 1
                l += 1
            if n == len(cnt):
                if not ans or len(ans) > r - l + 1:
                    ans = s[l: r+1]
        return ans


