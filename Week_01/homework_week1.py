#283移零,方法一
class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        k=0
        j=0
        for i in range(n):
            if nums[i]==0:
                nums.append(0)
        k=n
        while j<k:
            if nums[j]==0:
                nums.pop(j)
                k-=1
            else:
                j+=1
#283移零,方法二
class Solution(object):
    def moveZeroes(self,nums):
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                if i!=j:
                    nums[i]=0
                j+=1

#1两数之和,方法一
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=i
            if target-nums[i] in dic and i!=dic[target-nums[i]]:
                return [i,dic[target-nums[i]]]
#1两数之和,方法二
class Solution:
    def twoSum(self,nums:List[int],target:int):
        dict={}
        for i in range(len(nums)):
            if dict.get(target-nums[i]) is not None:
                return [dict.get(target-nums[i]),i]
            dict[nums[i]]=i

#21合并两个有序链表(递归理解起来很困难，有没有好的方法帮助理解）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2