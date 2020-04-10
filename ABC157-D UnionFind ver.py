import sys
sys.setrecursionlimit(4100000)

#Union Findデータ構造
class UnionFind:
    def __init__(self, n):
        #Data: 正:親要素のノード番号, 負:サイズ
        self.D = [-1 for i in range(n)]
    
    def find(self, x:int)->int:
        if self.D[x] < 0:
            return x
        else:
            self.D[x] = self.find(self.D[x])
            return self.D[x]

    
    def unite(self, x:int, y:int)->bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        else:
            if self.D[x] > self.D[y]:
                self.D[x], self.D[y] = self.D[y], self.D[x]
            else:
                pass
            self.D[x] += self.D[y]
            self.D[y] = x
            return True

    def same(self, x:int, y:int)->bool:
        return self.find(x) == self.find(y)

    def size(self, x:int)->int:
        return -self.D[self.find(x)]

n, m, k = map(int, input().split())

uf = UnionFind(n)  

CF = [0] * n #Count Friend
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    CF[a] += 1
    CF[b] += 1
    uf.unite(a, b)

CBinG = [0] * n #Count Block in Group
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if uf.same(c, d) == True:
        CBinG[c] += 1
        CBinG[d] += 1
    else:
        pass
    
for i in range(n):
    ans = uf.size(i) - 1 - CF[i] - CBinG[i]
    print(ans, end=' ')

