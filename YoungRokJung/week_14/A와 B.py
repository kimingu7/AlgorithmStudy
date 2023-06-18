import sys
input = sys.stdin.readline

S = input().rstrip()
T = list(input().rstrip())

# print(T)
words = [T]
while True :
    tmp = 0
    temp = []
    for word in words :
        # print(word)
        if len(word) == len(S) + 1 :
            tmp = 1
        if word[-1] == 'A' :
            temp.append(word[:-1])
        elif word[-1] == 'B' :
            word.pop()
            temp.append(list(reversed(word)))

    # print(temp)
    if tmp :
        for word in temp :
            if ''.join(word) == S :
                print(1)
                exit()
        else :
            print(0)
            break
    words = temp

# 되는지 안되는지만 확인하면 되므로 T에서 S로 갈 수 있는지 확인
# 역순으로 확인할 때 순서 잘 생각 !