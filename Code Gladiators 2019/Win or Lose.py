''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    t = int(input())
    
    for j in range(t):
        n = int(input())
        
        strengths = list(map(int,input().split()))
        energies = list(map(int,input().split()))

        strengths.sort()
        energies.sort()

        for i in range(n):
            if energies[i] <= strengths[i]:
                print('LOSE')
                break
        else:
            print('WIN')
    

main()

