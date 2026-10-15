import sys, re

def main():
    nums = list(map(int, re.findall(r'-?\d+', sys.stdin.read())))
    n = nums[0]
    segs = []
    p = 1
    for _ in range(n):
        if p + 4 > len(nums):
            break
        segs.append(tuple(nums[p:p+4])); p += 4
    if p + 2 > len(nums):
        print(0)
        return
    house = (nums[p], nums[p+1])

    pts = {house}
    for x1, y1, x2, y2 in segs:
        pts.add((x1, y1)); pts.add((x2, y2))
    for a in segs:
        for b in segs:
            if a[1] == a[3] and b[0] == b[2]:
                x, y = b[0], a[1]
                if min(a[0], a[2]) <= x <= max(a[0], a[2]) and \
                   min(b[1], b[3]) <= y <= max(b[1], b[3]):
                    pts.add((x, y))

    edges = set()
    for x1, y1, x2, y2 in segs:
        on = []
        for (x, y) in pts:
            if (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) == 0 and \
               min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                on.append((x, y))
        on.sort()
        for i in range(len(on) - 1):
            edges.add((on[i], on[i+1]))

    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)

    if house not in adj:
        print(0)
        return

    sys.setrecursionlimit(10000)
    visited = {house}
    count = 0

    def dfs(u, length):
        nonlocal count
        for w in adj[u]:
            if w == house:
                if length >= 2:
                    count += 1
            elif w not in visited:
                visited.add(w)
                dfs(w, length + 1)
                visited.discard(w)

    dfs(house, 0)
    print(count // 2)

main()