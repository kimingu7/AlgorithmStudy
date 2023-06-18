import sys
input = sys.stdin.readline
S = input().strip()
T = input().strip()

# 거꾸로 T를 끝에서부터 하나씩 자르기
while len(S) != len(T):
    if T[-1] == 'B':
        T = T[:-1][::-1]
    else:
        T = T[:-1]

if S == T:
    print(1)
else:
    print(0)