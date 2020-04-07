x, y, a, b, c = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

pnum, qnum, rnum = 0, 0, 0
ans = 0
time = 0
while time < x+y:
    #P, Q, Rのなかで現状最大の値を取り出す(x,yの値も考慮)
    #P
    if pnum >= x:
        p = 0
    else:
        p = P[pnum]
    #Q
    if qnum >= y:
        q = 0
    else:
        q = Q[qnum]
    #R
    if rnum >=  c:
        r = 0
    else:
        r = R[rnum]
    Option = [p, q, r]

    #今の状況の中でおいしさ最大のものを取り出す
    m = 0
    color = 0
    for i in range(3):
        if m < Option[i]:
            m = Option[i]
            color = i
        else:
            pass
    ans += m

    #選択済みのリンゴを反映
    if color == 0:
        pnum += 1
    elif color == 1:
        qnum += 1
    elif color == 2:
        rnum += 1
    else:   
        print('error')

    #今まで選んだリンゴの数を反映
    time += 1

print(ans)