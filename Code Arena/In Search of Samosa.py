n, k = map(int,input().split())

arr = list(map(int,input().split()))

asum = 0
count = 0

arr.sort()

for i in range(n):
    if arr[i]+asum <= k: 
        asum += arr[i]
        count += 1
    else:
        break

print(count)