# UVA 531 - Compromise
# https://onlinejudge.org/external/5/531.pdf
#
# Find the longest common subsequence (LCS) of two sequences of words.
# Standard LCS with backtracking to reconstruct the actual subsequence.

import sys

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    while idx < len(data):
        # Read first text until '#'
        words1 = []
        while idx < len(data):
            line = data[idx].strip()
            idx += 1
            if line == '#':
                break
            words1.extend(line.split())
        
        if not words1:
            break
        
        # Read second text until '#'
        words2 = []
        while idx < len(data):
            line = data[idx].strip()
            idx += 1
            if line == '#':
                break
            words2.extend(line.split())
        
        m, n = len(words1), len(words2)
        # LCS DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if words1[i - 1] == words2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Backtrack to find the LCS
        result = []
        i, j = m, n
        while i > 0 and j > 0:
            if words1[i - 1] == words2[j - 1]:
                result.append(words1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        
        result.reverse()
        print(' '.join(result))

if __name__ == "__main__":
    solve()
