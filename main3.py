n = int(input())
s = list(input())

t = []
for i in range(n):
    if s < list(reversed(s)):
        t.append(s[0])
        s = s[1:]
    else:
        t.append(s[-1])
        s = s[:-1]

print(''.join(t))