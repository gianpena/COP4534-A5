s1 = input()
s2 = input()

m,n = len(s1), len(s2)
dp = [[-1 for j in range(n)] for i in range(m)]

def edit_distance(i,j):
    if i < 0: return 0 if i == j else j
    if j < 0: return 0 if i == j else i
    if dp[i][j] != -1: return dp[i][j]

    ans = (s1[i] != s2[j]) + edit_distance(i-1, j-1)
    ans = min(ans, 1 + edit_distance(i-1, j))
    ans = min(ans, 1 + edit_distance(i, j-1))

    dp[i][j] = ans
    return ans

print(edit_distance(m-1,n-1))
