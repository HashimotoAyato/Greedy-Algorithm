n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

task = dict(zip(t,s))
task = sorted(task.items())

time = count = 0
for i in range(len(task)):
    if time < task[i][1]:
        time = task[i][0]
        count += 1

print(count)