def mask(n):
    mask = 0
    i = 1
    while n//i:
        digit = n/i % 10
        mask |= 1 << int(digit)
        i *= 10
    return mask

# set = a , memo = arr, a = alist
def dp(a,arr,alist):
    if a == 0:
        arr[a] = 0
        return arr[a]
    if arr[a] != -1:
        return arr[a]
    maxi = 0
    for num in alist:
        bitmask = mask(num)
        if ((a | bitmask) == a):
            maxi = max(dp(a ^ mask(num), arr, alist) + num, maxi)
    arr[a] = maxi
    return arr[a]

if __name__ == '__main__':
    li = [121,23,3,333,4]
    left = 1 << 10
    memo = [None] * left
    maxsum = 0
    for i in range(left): 
        memo[i] = -1
    for i in range(left): 
        maxsum = max(maxsum, dp(i, memo, li))
    print('Maximum = ',maxsum)
