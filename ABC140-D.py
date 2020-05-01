n , k = map(int, input().split())
S = input()

fs = 0  #first score
for i in range(n-1):
    if S[i] == S[i + 1]:
        fs += 1
    else:
        pass

ans = min(n - 1, fs + 2 * k)
print(ans)