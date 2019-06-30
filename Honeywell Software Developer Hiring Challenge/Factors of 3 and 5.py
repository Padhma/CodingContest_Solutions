def findIdeal(l,r):
    count = 0
    for i in range(l,r+1):
        num = i
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        if num == 1:
            count += 1
    return count

if __name__ == "__main__":
    l = 1
    r = 10
    
    print(findIdeal(l,r))