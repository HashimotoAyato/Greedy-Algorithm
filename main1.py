coin_num = list(map(int, input().split()))
a = int(input())
coin_value = [1,5,10,50,100,500]

total = 0
count = 0
for i in reversed(range(len(coin_num))):
    if int((a-total) / coin_value[i]) <= coin_num[i]:
        count += int((a-total) / coin_value[i])
        total += int((a-total) / coin_value[i]) * coin_value[i]
    else:
        count += coin_num[i]
        total += coin_num[i] * coin_value[i]

print(count)