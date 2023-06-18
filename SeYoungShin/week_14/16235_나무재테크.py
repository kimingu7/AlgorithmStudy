import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] * N for _ in range(N)] for _ in range(N)]
nutr = [[5] * N for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
while K:
    dietree = [[[] * N for _ in range(N)] for _ in range(N)]
    newtree = [[0] * N for _ in range(N)]
    # 나이순 정렬
    for i in range(N):
        for j in range(N):
            tree[i][j].sort()

    # 봄
    for i in range(N):
        for j in range(N):
            k = 0
            while k != len(tree[i][j]):
                if nutr[i][j] >= tree[i][j][k]:
                    nutr[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                    k += 1
                else:
                    die = tree[i][j].pop(k)
                    dietree[i][j].append(die)

    # 여름
    for i in range(N):
        for j in range(N):
            for k in range(len(dietree[i][j])):
                nutr[i][j] += dietree[i][j][k] // 2

    # 가을
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for l in range(8):
                        ni, nj = i + di[l], j + dj[l]
                        if 0 <= ni < N and 0 <= nj < N:
                            newtree[ni][nj] += 1
    for i in range(N):
        for j in range(N):
            for k in range(newtree[i][j]):
                tree[i][j].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            nutr[i][j] += A[i][j]

    # 1년 지남
    K -= 1

# 나무 수 세기
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)