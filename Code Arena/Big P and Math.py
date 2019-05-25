a, b = map(str,input().split())
b1 = a.replace('5','6')
b2 = b.replace('5','6')
c = a.replace('6','5')
c1 = b.replace('6','5')

print(int(c)+int(c1),int(b1)+int(b2))
