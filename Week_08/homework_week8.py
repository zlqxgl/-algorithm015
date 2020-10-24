#位1的个数
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=n&1
            n>>=1
        return res

#2的幂
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

#1122数组的相对排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        ans = []
        for i in range(len(arr1)):
            arr[arr1[i]] += 1
        for i in range(len(arr2)):
            while arr[arr2[i]] > 0:
                ans.append(arr2[i])
                arr[arr2[i]] -= 1
        for i in range(len(arr)):
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans


#56合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res


#493翻转对
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        tb, res = [], 0
        for n in reversed(nums) :
            res += bisect.bisect_left(tb, n)
            n2 = 2*n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)
        return res




