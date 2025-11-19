print("Please enter the number of nodes and edges in your graph, separated by a single space: ", end='')
n,e = map(int, input().split())

print("For the next e lines, please enter the two nodes the edge joins, and the edge weight, separated by a single space.")
print("Please note that the graph is directed.")
dp = [[float('inf') for j in range(n)] for i in range(n)]
for u in range(n):
  dp[u][u] = 0
for _ in range(e):
  u,v,w = map(int, input().split())
  dp[u][v] = min(dp[u][v], w)

for k in range(n):
  for i in range(n):
    for j in range(n):
      if dp[i][k] + dp[k][j] < dp[i][j]:
        dp[i][j] = dp[i][k] + dp[k][j]

if any(dp[u][u] < 0 for u in range(n)):
  print('\nNegative weight cycle detected!')
  exit(0)

print('')
for i in range(n):
  for j in range(n):
    print(f'{i} -> {j}: ', end='')
    if dp[i][j] == float('inf'):
      print('impossible')
    else:
      print(dp[i][j])