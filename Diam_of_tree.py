# variables
n = int(input())
gr = [[] for _ in range(n)]


# functions
def dfs(v, ans, p=-1):
    if p == -1:
        ans[v] = 0
    else:
        ans[v] = ans[p] + 1
    for u in gr[v]:
        if u != p:
            dfs(u, ans, v)


def far(v):
    return dfs(v, [i for i in range(v)])


# main
for i in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    gr[u].append(v)
    gr[v].append(u)

d1 = far(0)
v = max(d1)
