n = int(input())
l = list(map(int, input().split()))

l.sort()
cost = 0
while 1 < len(l):
    l[1] = l[0] + l[1]
    l = l[1:]
    cost += l[0]

print(cost)