from collections import deque
n, x, y = map(int, input().split())

def push(v, d):
    if Dist[v] == -1:   #距離未更新
        Dist[v] = d
        Queue.append(v)
    else:   #距離が更新済み
        pass
    return 0
    
Ans = [0] * n
for i in range(n):
    Queue = deque([i])
    Dist = [-1] * n
    Dist[i] = 0 
    while len(Queue) != 0:
        v = Queue[0]
        d = Dist[v]
        #辺を通して次の頂点へ

        #-方向
        if v-1 >= 0:
            push(v-1, d+1)
        else:
            pass

        #+方向
        if v+1 < n:
            push(v+1, d+1)
        else:
            pass

        #XとYの間
        if v == x-1 :
            push(y-1, d+1)
        elif v == y-1:
            push(x-1, d+1)
        else:
            pass
        Queue.popleft()
    for i in Dist:
        Ans[i] += 1

for i in range(len(Ans)):
    Ans[i] *= 0.5

for i in range(1, n):
    print(int(Ans[i]))


