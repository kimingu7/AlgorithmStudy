import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline

n = int(input())
scv = list(map(int, input().split()))
ans = 0
if n == 1:
    if scv[0] <= 9:
        ans = 1
    else:
        ans = scv[0] // 9 + 1
    print(ans)
else:
    if n == 2:
        scv.append(0)

    m = max(scv)
    dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)]
    # 각 scv 피를 나타낸다. dp[i][j][k] = 5 -> 피가 i,j,k 남은 scv가 되기까지 5번 공격
    dp[scv[0]][scv[1]][scv[2]] = 1
    hp = [1, 3, 9]
    HP = list(permutations(hp, 3))

    for i in range(m, -1, -1):
        for j in range(m, -1, -1):
            for k in range(m, -1, -1):
                if dp[i][j][k]:
                    for p in HP:
                        i_ = i - p[0] if i - p[0] >= 0 else 0
                        j_ = j - p[1] if j - p[1] >= 0 else 0
                        k_ = k - p[2] if k - p[2] >= 0 else 0
                        if dp[i_][j_][k_] == 0 or dp[i_][j_][k_] > dp[i][j][k] + 1:
                            dp[i_][j_][k_] = dp[i][j][k] + 1

    print(dp[0][0][0] - 1)
