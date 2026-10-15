
from collections import Counter

target = input().strip()
n = int(input())
words = input().split()
costs = list(map(int, input().split()))

m = len(target)
INF = float('inf')

# Case 1: Letters inside each piece can be rearranged
dp1 = [INF] * (m + 1)
dp1[0] = 0

for i in range(m):
    if dp1[i] == INF:
        continue

    for word, cost in zip(words, costs):
        counts = Counter(word)
        j = i
        used = Counter()

        while j < m and used[target[j]] < counts[target[j]]:
            used[target[j]] += 1
            j += 1

        if j > i:
            dp1[j] = min(dp1[j], dp1[i] + cost)

# Case 2: Letters must remain in their original order
dp2 = [INF] * (m + 1)
dp2[0] = 0

for i in range(m):
    if dp2[i] == INF:
        continue

    for word, cost in zip(words, costs):
        j = i

        for ch in word:
            if j < m and ch == target[j]:
                j += 1

        if j > i:
            dp2[j] = min(dp2[j], dp2[i] + cost)

if dp1[m] == INF or dp2[m] == INF:
    print(-1)
else:
    print(dp2[m] - dp1[m])
