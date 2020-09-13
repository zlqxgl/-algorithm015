#236二叉树的最近公共祖先
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res_p = []#存储根节点到目标点路径
        res_q = []
        def back(node, path, target, res):
            if not node:
                return
            if node == target:
                path.append(node)
                res.extend(path[:])
                return
            path.append(node)
            back(node.left, path, target, res)
            back(node.right, path, target, res)
            path.pop()  # 记得恢复状态

        back(root, [], p, res_p)#回溯法获取根节点到目标点路径
        back(root, [], q, res_q)
        # 让 res_p 存储路径较小的那个，方便下面遍历查找操作
        if len(res_p) > len(res_q):
            res_p, res_q = res_q, res_p
        for i in range(len(res_p)):
            if res_p[i] != res_q[i]:
                if i > 0:
                    return res_p[i - 1]
                elif i == 0:
                    return res_p[i]
        return res_p[-1]#用于判定较短路径包含在较长路径的情况

#105从前序和中序遍历构造二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:return None
        root=TreeNode(preorder[0])
        idx=inorder.index(preorder[0])
        #上面idx为左子树长度，根据中序遍历确定左右子树长度
        root.left=self.buildTree(preorder[1:1+idx],inorder[:idx])
        root.right=self.buildTree(preorder[1+idx:],inorder[idx+1:])
        return root
#77组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i for i in range(1,n+1)]
        res=[]
        def backtrace(num,curr,index):
            if len(curr)==k:
                res.append(curr[:])
            for i in range(index,n):
                backtrace(num[index:],curr+[nums[i]],i+1)
        if n==0 or k==0:
            return res
        backtrace(nums,[],0)
        return res

#46全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(nums,temp):
            if not nums:
                res.append(temp)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],temp+[nums[i]])
        backtrack(nums,[])
        return res

#47全排列2
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrace(nums,temp):
            if not nums:
                res.append(temp)
            visited=set()
            for i in range(len(nums)):
                if nums[i] in visited:continue
                backtrace(nums[:i]+nums[i+1:],temp+[nums[i]])
                visited.add(nums[i])
        backtrace(nums,[])
        return res
