import sys
import re

while True:
    s = sys.stdin.readline()
    if len(s) >= 2:
        if '//' in s:
            s = re.split("//",s)
            s[0] = re.sub("->",".",s[0])
            sys.stdout.write('//'.join(s))
        else:
            sys.stdout.write(re.sub("->",".",s))
    else:
        break