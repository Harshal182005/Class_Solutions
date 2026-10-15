def main():
    t = input().strip()
    X, Y = map(int, input().split())

    seg = {
        '0': set("abcdef"), '1': set("bc"), '2': set("abdeg"),
        '3': set("abcdg"), '4': set("bcfg"), '5': set("acdfg"),
        '6': set("acdefg"), '7': set("abc"), '8': set("abcdefg"),
        '9': set("abcdfg"),
    }

    # digit -> digits reachable by toggling exactly one segment
    nxt = {d: [e for e in seg if len(seg[d] ^ seg[e]) == 1] for d in seg}

    h0, m0 = int(t[:2]), int(t[3:])
    best = None
    for pos in (0, 1, 3, 4):
        for nd in nxt[t[pos]]:
            s = t[:pos] + nd + t[pos + 1:]
            h, m = int(s[:2]), int(s[3:])
            if not (1 <= h <= 12 and 0 <= m <= 59):
                continue
            dh = abs(h - h0) % 12
            dh = min(dh, 12 - dh)          # hour hand moves in whole hours, either direction
            dm = abs(m - m0)
            dm = min(dm, 60 - dm)          # minute hand moves either direction
            cost = dh * 5 * X + dm * Y     # one hour step = 5 minute marks
            if best is None or (cost, s) < best:
                best = (cost, s)

    print(best[1] if best else "No closest valid time possible")

main()