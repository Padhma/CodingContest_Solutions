t = int(input())
asum = 0
asub = 0

for _ in range(t):
    n,better,worse = map(int,input().split())
    asum = n-better
    asub = worse + 1
    if asum == worse:
        print(worse)
    else:
        print(asub)