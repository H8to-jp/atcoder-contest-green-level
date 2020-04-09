from collections import Counter
import sys
sys.setrecursionlimit(4100000)

n, m, k = map(int, input().split())

#友達関係
F = [[] for i in range(n)] #Friend
for i in range(m):
    a, b = map(int, input().split())
    F[a-1].append(b)
    F[b-1].append(a)

#DFSで連結部分ごとのグループに分ける
G = [0] * n #Group
gid = 0 #group id

#DFSを行うための関数
def using_DFS(p):
    if G[p] == 0:
        G[p] = gid
        for j in F[p]:
            if G[j-1] == 0:
                using_DFS(j-1)
            else:   #すでに登場
                pass
    else:
        pass

for i in range(n):
    if G[i] == 0:
        gid += 1
        using_DFS(i)
    else:
        pass

#ブロック関係
BinG = [[] for i in range(n)] #Block in Group
for i in range(k):
    c, d = map(int, input().split())
    if G[c-1] == G[d-1]:
        BinG[c-1].append(d)
        BinG[d-1].append(c)
    else:
        pass

GS = Counter(G) #Group Size
for i in range(n):
    #G[i]:その人が所属するGroupのid
    #GS[G[i]]:その人が所属するGroupの連結サイズ
    #len(F[i]):すでに友達になっている数
    #len(BinG[i]):その人が所属するGroupでブロックしている人数
    ans =  GS[G[i]] - 1 - len(F[i]) - len(BinG[i])
    print(ans)