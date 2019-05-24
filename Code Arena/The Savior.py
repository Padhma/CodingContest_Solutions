t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    
    count = 0
    
    for i in range(n):
        for j in range(i+1,n):
            asum = l[i] + l[j]
            if l[i] != l[j] and asum % 2 == 0:
                count += 1
    
    print(count)