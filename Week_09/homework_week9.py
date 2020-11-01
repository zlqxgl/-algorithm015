#387字符串的第一个唯一字符
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

#541反转字符串2
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, flag = "", True
        for i in range(0, len(s), k):
            res += s[i:i + k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res

#557反转字符串中的单词3
class Solution(object):
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split(" "))

#917仅仅反转字母
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        slist = list(S)
        front,end = 0,len(slist)-1
        while front < end:
            if not slist[front].isalpha():
                front +=1
            elif not slist[end].isalpha():
                end -=1
            else:
                slist[front],slist[end]=slist[end],slist[front]
                front +=1
                end -=1
        return ''.join(slist)

#300最长上升子序列
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

#438找到字符串中的所有字母异位词
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        n = len(p)
        p = Counter(p)
        dp = [0] * (len(s) + 1)
        dp[0] = Counter()
        res = []
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1].copy()
            dp[i][s[i - 1]] += 1
            if i >= n and dp[i] - dp[i - n] == p:
                res.append(i - n)
        return res

#32最长有效括号
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        cur = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length

#115不同的子序列
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]

