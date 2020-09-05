#242有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        return collections.Counter(s)==collections.Counter(t)

#589N叉树的前序遍历
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            s.extend(node.children[::-1])
        return res


#49字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            temp="".join(sorted(list(i)))
            if temp in res.keys():
                res[temp].append(i)
            else:
                res[temp]=[i]
        return list(res.values())

#144二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)

#94二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)

#49丑数
class Solution:
    import heapq
    def nthUglyNumber(self, n: int) -> int:
        res = []
        ls = [1]
        heapq.heapify(ls)
        for _ in range(n):
            cur = heapq.heappop(ls)
            res.append(cur)
            cur1, cur2, cur3 = cur*2, cur*3, cur*5
            setls = set(ls)
            setTmp = {cur1,cur2,cur3}
            diff = setTmp.difference(setls)
            print(diff)
            if diff:
                for item in diff:
                    heapq.heappush(ls,item)
        return res[-1]



#347前K个高频元素
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap, ans = [], []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans