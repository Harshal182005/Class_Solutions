import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    p = 0
    N, M = int(data[p]), int(data[p + 1]); p += 2   # N = width (x), M = height (y)
    L = int(data[p]); p += 1

    hwall = set()   # (x, y): wall between cell (x, y-1) and (x, y)
    vwall = set()   # (x, y): wall between cell (x-1, y) and (x, y)
    for _ in range(L):
        x1, y1, x2, y2 = (int(v) for v in data[p:p + 4]); p += 4
        if y1 == y2:                                  # horizontal segment
            for x in range(min(x1, x2), max(x1, x2)):
                hwall.add((x, y1))
        else:                                         # vertical segment
            for y in range(min(y1, y2), max(y1, y2)):
                vwall.add((x1, y))

    R = int(data[p]); p += 1
    strs = data[p:]

    seen = [[False] * M for _ in range(N)]
    boxes = []   # (area, min_x, min_y)
    for sx in range(N):
        for sy in range(M):
            if seen[sx][sy]:
                continue
            seen[sx][sy] = True
            dq = deque([(sx, sy)])
            area, mx, my = 0, sx, sy
            while dq:
                x, y = dq.popleft()
                area += 1
                mx, my = min(mx, x), min(my, y)
                # right
                if x + 1 < N and not seen[x + 1][y] and (x + 1, y) not in vwall:
                    seen[x + 1][y] = True; dq.append((x + 1, y))
                # left
                if x - 1 >= 0 and not seen[x - 1][y] and (x, y) not in vwall:
                    seen[x - 1][y] = True; dq.append((x - 1, y))
                # up
                if y + 1 < M and not seen[x][y + 1] and (x, y + 1) not in hwall:
                    seen[x][y + 1] = True; dq.append((x, y + 1))
                # down
                if y - 1 >= 0 and not seen[x][y - 1] and (x, y) not in hwall:
                    seen[x][y - 1] = True; dq.append((x, y - 1))
            boxes.append((area, mx, my))

    # string placement order: left to right, then bottom to top
    order = sorted(range(len(boxes)), key=lambda i: (boxes[i][2], boxes[i][1]))
    string_of = {box: strs[k] for k, box in enumerate(order)}

    # rank order: larger area, then smaller x, then smaller y
    ranked = sorted(range(len(boxes)), key=lambda i: (-boxes[i][0], boxes[i][1], boxes[i][2]))
    target = ranked[R - 1]
    print(sum(ord(c) for c in strs[order.index(target)]))

main()