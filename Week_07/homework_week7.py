#203实现Tire(前缀树）
class Trie:
    def __init__(self):
        self.root={}
        self.end_of_word="#"

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.end_of_word]=self.end_of_word

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if char not in node:
                return False
            node=node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            if char not in node:
                return False
            node=node[char]
        return True
#547朋友圈
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent = [-1 for _ in range(len(M))]

        def find(parent, i):
            if parent[i] == -1: return i
            return find(parent, parent[i])

        def union(parent, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if xroot != yroot:
                parent[xroot] = yroot

        def union_find(Matrix):
            for i in range(len(Matrix)):
                for j in range(len(Matrix)):
                    if Matrix[i][j] == 1 and i != j:
                        union(parent, i, j)
            count = 0
            for i in range(len(parent)):
                if parent[i] == -1:
                    count += 1
            return count
        return union_find(M)
#36有效的数独
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hang_dic=[[]for i in range(9)]
        lie_dic=[[]for j in range(9)]#也可以构建一个9*9的列表
        kuai_dic=[[]for e in range(9)]
        for i in range (9):
            for j in range(9):
                num=board[i][j]
                kuai=i//3*3+j//3
                if num!='.':
                    num=int(num)
                    if num not in hang_dic[i]:
                        hang_dic[i].append(num)
                    else:
                        return False
                    if num not in lie_dic[j]:
                        lie_dic[j].append(num)
                    else:
                        return False
                    if num not in kuai_dic[kuai]:
                        kuai_dic[kuai].append(num)
                    else:
                        return False
        return True

#212单词搜索2
dx=[-1,1,0,0]
dy=[0,0,-1,1]
END_OF_WORD="#"
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:return []
        if not words:return []
        self.result=set()

        root=collections.defaultdict()
        for word in words:
            node= root
            for char in word:
                node =node.setdefault(char,collections.defaultdict())
            node[END_OF_WORD]=END_OF_WORD

        self.m,self.n=len(board),len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board,i,j,"",root)
        return list(self.result)
    def _dfs(self,board,i,j,cur_word,cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        tmp,board[i][j] = board[i][j],'@'
        for k in range(4):
            x,y=i+dx[k],j+dy[k]
            if 0<= x < self.m and 0<= y < self.n and board[x][y] !="@" and board[x][y] in cur_dict:
                self._dfs(board,x,y,cur_word,cur_dict)
        board[i][j]=tmp




