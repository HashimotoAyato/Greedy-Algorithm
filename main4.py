n = int(input())
r = int(input())
x = list(map(int, input().split()))

count = i = 0
while i < n-1:
    j = i
    while x[j+1] - x[i] <= r:
        j += 1
    count += 1
    i = j + 1

print(count)
