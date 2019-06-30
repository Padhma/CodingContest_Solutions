s = ['code','doce','ecod','framer','frame']

for i in range(len(s)-1):
    j = i+1
    while j < len(s):
        if sorted(s[i]) == sorted(s[j]):
            s.remove(s[j])
        else:
            j += 1
s.sort()
print(s)