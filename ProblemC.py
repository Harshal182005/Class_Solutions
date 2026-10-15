import sys, heapq
from collections import deque

def main():
    data = sys.stdin.read().split()
    N, M = int(data[0]), int(data[1])
    rest = "".join(data[2:])
    grid = [rest[i*N:(i+1)*N] for i in range(N)]
    K = N // M

    def rot(sh):
        return tuple("".join(sh[M-1-j][i] for j in range(M)) for i in range(M))

    sheets = []
    sid = did = -1
    for bi in range(K):
        for bj in range(K):
            sh = tuple(grid[bi*M+r][bj*M:(bj+1)*M] for r in range(M))
            flat = "".join(sh)
            idx = len(sheets)
            if 'S' in flat: sid = idx
            if 'D' in flat: did = idx
            rots = [sh]
            for _ in range(3):
                rots.append(rot(rots[-1]))
            sheets.append(rots)

    # BFS inside a sheet from a cell: returns dict cell->dist
    cache = {}
    def reach(s, r, start):
        key = (s, r, start)
        if key in cache:
            return cache[key]
        sh = sheets[s][r]
        dist = {start: 0}
        dq = deque([start])
        while dq:
            x, y = dq.popleft()
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                a, b = x+dx, y+dy
                if 0 <= a < M and 0 <= b < M and (a, b) not in dist and sh[a][b] != 'L':
                    dist[(a, b)] = dist[(x, y)] + 1
                    dq.append((a, b))
        cache[key] = dist
        return dist

    def find(sh, ch):
        for i in range(M):
            for j in range(M):
                if sh[i][j] == ch:
                    return (i, j)

    last = (K-1, K-1)
    pq = []
    seen = set()
    cnt = 0
    for r in range(4):
        st = find(sheets[sid][r], 'S')
        heapq.heappush(pq, (0, cnt, 0, 0, sid, r, st, 1 << sid, 1, False))
        cnt += 1

    while pq:
        d, _, pr, pc, s, r, cell, mask, pmask, term = heapq.heappop(pq)
        if term:
            print(d)
            return
        key = (pr, pc, s, r, cell, mask, pmask)
        if key in seen:
            continue
        seen.add(key)
        dm = reach(s, r, cell)
        sh = sheets[s][r]
        if s == did and (pr, pc) == last:
            for (x, y), dd in dm.items():
                if sh[x][y] == 'D':
                    heapq.heappush(pq, (d + dd, cnt, 0, 0, 0, 0, None, 0, 0, True))
                    cnt += 1
            continue
        for (x, y), dd in dm.items():
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                a, b = x+dx, y+dy
                if 0 <= a < M and 0 <= b < M:
                    continue
                npr, npc = pr+dx, pc+dy
                if not (0 <= npr < K and 0 <= npc < K):
                    continue
                pbit = 1 << (npr*K+npc)
                if pmask & pbit:
                    continue
                ec = (a % M, b % M)
                isl = (npr, npc) == last
                for s2 in range(len(sheets)):
                    if mask >> s2 & 1:
                        continue
                    if s2 == sid:
                        continue
                    if (s2 == did) != isl:
                        continue
                    for r2 in range(4):
                        if sheets[s2][r2][ec[0]][ec[1]] == 'L':
                            continue
                        heapq.heappush(pq, (d + dd + 1, cnt, npr, npc, s2, r2, ec,
                                            mask | (1 << s2), pmask | pbit, False))
                        cnt += 1
    print(-1)

main()