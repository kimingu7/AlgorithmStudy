import sys, heapq
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
point = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

graph= [[deque() for _ in range(n)] for _ in range(n)]
visited = [[5]*n for _ in range(n)]

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x-1][y-1].append(z)

def SpringSummer(): # 봄,여름
    visited_die = [[0]*n for _ in range(n)] # 죽은 나무 저장
    # 봄
    for i in range(n):
        for j in range(n):
            if graph[i][j] :
                tree = []
                k = len(graph[i][j])
                # print(i,j,k,graph[i][j])
                for _ in range(k) :
                    a = graph[i][j].popleft()
                    # print(a)
                    if a > visited[i][j] :
                        visited_die[i][j] += a//2
                    else :
                        tree.append(a+1)
                        visited[i][j] -= a
                for l in tree :
                    graph[i][j].append(l)

    # 여름
    for i in range(n):
        for j in range(n):
            visited[i][j] += visited_die[i][j]

    return

def fall(): # 가을
    for i in range(n):
        for j in range(n):
            for k in range(len(graph[i][j])) :
                if graph[i][j][k] % 5 == 0 :
                    for di,dj in point :
                        ni,nj = i+di, j+dj
                        if 0<=ni<n and 0<=nj<n :
                            graph[ni][nj].appendleft(1)

    return

def winter(): # 겨울
    for i in range(n):
        for j in range(n):
            visited[i][j] += A[i][j]
    return

for l in range(k) :
    SpringSummer()
    fall()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(graph[i][j])
print(ans)

# 처음에 문제에서 제일 나이가 작은 나무부터 양분 섭취한다해서 heapq 최소힙으로 구현 -> 답은 맞지만 시간초과
# 잘 생각해보니 그냥 deque의 appendleft popleft 로 구현 가능 -> 아무리 heapq라도 정렬하는 시간 때문에 시간 더 걸리는듯(?)