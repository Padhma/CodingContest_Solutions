''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        integerList = list(map(int,input().split()))

        maxsum = 0
        for i in range(n):
            ele = i+2
            if ele != n:
                new_sum = integerList[i] + integerList[ele]
                if new_sum > maxsum:
                    maxsum = new_sum
                    first = integerList[i]
                    last = integerList[ele]
                ele += 1
            else:
                break
    
        listMax = max(integerList)
        if first+last > listMax:
            print(last,first,sep='')
        else:
            print(listMax)

main()

