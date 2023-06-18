def BFS():
    stack = deque()
    stack.append(SCV)
    visit[SCV[0]][SCV[1]][SCV[2]] = 1

    while stack:
        x, y, z = stack.popleft()
        if x == 0 and y == 0 and z == 0:
            print(visit[x][y][z] - 1)
            break

        for i, j, k in permu:
            nextH = []
            for now, order in ((x, i), (y, j), (z, k)):
                nextH.append(now - loseH[order] if now - loseH[order] >= 0 else 0)
            nextH.sort(reverse = True)
            nx, ny, nz = nextH

            if not visit[nx][ny][nz]:
                visit[nx][ny][nz] = visit[x][y][z] + 1
                stack.append((nx, ny, nz))


from collections import deque
from itertools import permutations
N = int(input())
SCV = list(map(int, input().split())) + [0] * (3 - N)
SCV.sort(reverse = True)

# 공격하는 순서와 잃는 체력
permu = list(permutations((0, 1, 2), 3))
loseH = (9, 3, 1)

# 3차원 배열로 방문 체크 및 BFS
maxH = max(SCV) + 1
visit = [[[0] * maxH for _ in range(maxH)] for _ in range(maxH)]
BFS()