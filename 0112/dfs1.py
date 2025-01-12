#n과m

N, M = map(int, input().split())
ans = []
visited = [0] * (N+1)

def back():
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, N+1):
        if visited[i] == 1:
            continue
        visited[i] = 1
        ans.append(i)
        back()
        ans.pop()
        visited[i] = 0

back()


