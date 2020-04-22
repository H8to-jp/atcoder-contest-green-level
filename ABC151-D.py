from collections import deque
h, w = map(int, input().split())
S = [0 for i in range(h)]
for i in range(h):
    S[i] = input()

Di = [-1, 1, 0, 0] #Direction i
Dj = [0, 0, -1, 1] #Direction j
inf = 1000  #十分大きな数

def update_data(i:int, j:int, x:int):
    if Dist[i][j] == inf:
        Dist[i][j] = x
        Q.append([i, j])
    else:
        pass

ans = 0
for si in range(h):
    for sj in range(w):
        Dist = [[inf for j in range(w)] for i in range(h)]   #Distance
        if S[si][sj] == '.':
            Q = deque([])
            update_data(si, sj, 0)
            #BFS
            while len(Q) != 0:
                i, j  = Q[0][0], Q[0][1]
                Q.popleft()
                for dr in range(4):
                    ni , nj = i+Di[dr], j+Dj[dr]
                    if 0 <= ni and ni < h and 0 <= nj and nj < w:
                        if S[ni][nj] == '.':
                            update_data(ni, nj, Dist[i][j]+1)
                        else:
                            pass
                    else:
                        pass
            for i in range(h):
                for j in range(w):
                    if Dist[i][j] == inf:
                        pass
                    else:    
                        if ans < Dist[i][j]:
                            ans = Dist[i][j]
                        else:
                            pass
        else:
            pass
print(ans)