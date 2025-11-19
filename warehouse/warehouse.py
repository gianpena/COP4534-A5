print("Please enter the number of distinct items available for purchase: ", end='')
n = int(input())

print("Please enter the weight limit for all items purchased: ", end='')
W = int(input())
print("For each of the next n lines of input, enter:\n" \
"1) The cost of procuring this item\n" \
"2) The revenue this item generates\n" \
"3) The weight of this item\n" \
"each separated by a single space.")

items = []
for i in range(n):
  cost,revenue,weight = map(int, input().split())
  items.append((cost,revenue,weight))

dp = [[-1 for j in range(W+1)] for i in range(n)]

for i in range(n):
  dp[i][0] = 0

for w in range(W+1):
  dp[n-1][w] = items[n-1][1] - items[n-1][0] if w >= items[n-1][2] else 0

for i in range(n-2, -1, -1):
  for w in range(1, W+1):
    if w >= items[i][2]: take = items[i][1] - items[i][0] + dp[i][w - items[i][2]]
    else: take = 0
    dont_take = dp[i+1][w]
    dp[i][w] = max(take, dont_take)

print(f'Maximum possible profit is {dp[0][W]}')