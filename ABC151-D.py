h, w = map(int, input().split())
S = [0 for i in range(h)]
P = []

for i in range(h):
    S[i] = input()
    for j in range(len(S[i])):
        if S[i][j] == '.':
            P.append([i, j])
        else:
            pass

MV = [[-1, 0], [1, 0], [0, -1], [0, 1]]   #Move Vectol
ans = 0
def print_field(L:list):
    for i in range(len(L)):
        print(L[i])
    
def try_move(ch:int, cw:int, M:list):
    if 0 <= ch and ch < h and 0 <= cw and cw < w:
        if M[ch][cw] == '.':
            return True
        else:
            pass
    else:
        pass
    return False

def search_root(ch:int, cw:int, time:int, M:list):
    global md
    #print('time = ', time)
    if ch == gh and cw == gw:
        #print('gtime = ',time)
        if time < md:
            md = time
        else:
            pass
    else:
        for i in range(4):
            if try_move(ch+MV[i][0], cw+MV[i][1], M) == True:
                R = M[:]
                R[ch+MV[i][0]] = R[ch+MV[i][0]][0:cw+MV[i][1]] + '〇' + R[ch+MV[i][0]][cw+MV[i][1]+1:]
                #print_field(R)
                search_root(ch+MV[i][0], cw+MV[i][1], time+1, R)
            else:
                pass

ans = 0
for i in range(len(P)):
    for j in range(i+1, len(P)):
        md = h*w
        F = S[:]
        sh, sw = P[i]
        gh, gw = P[j]
        search_root(sh, sw, 0, F)
        if ans < md:
            ans = md
        else:
            pass
print(ans)