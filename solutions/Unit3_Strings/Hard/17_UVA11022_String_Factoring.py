# UVA 11022 - String Factoring
# https://onlinejudge.org/external/110/11022.pdf
#
# Find the weight of maximal factoring of a string.
# DP approach: dp[i][j] = minimum weight (number of characters) to
# represent s[i..j]. For each substring, try all possible factorizations.

import sys

def solve():
    for line in sys.stdin:
        s = line.strip()
        if s == '*':
            break
        n = len(s)
        # dp[i][j] = min weight to represent s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1  # single character has weight 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # worst case: no compression
                
                # Try splitting into two parts
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                
                # Try repeating a prefix
                substr_len = j - i + 1
                for p in range(1, substr_len):
                    if substr_len % p == 0:
                        # Check if s[i:j+1] = (s[i:i+p]) repeated
                        pattern = s[i:i + p]
                        valid = True
                        for k in range(i + p, j + 1, p):
                            if s[k:k + p] != pattern:
                                valid = False
                                break
                        if valid:
                            dp[i][j] = min(dp[i][j], dp[i][i + p - 1])
        
        print(dp[0][n - 1])

if __name__ == "__main__":
    solve()
