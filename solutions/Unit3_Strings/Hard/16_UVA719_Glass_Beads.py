# UVA 719 - Glass Beads
# https://onlinejudge.org/external/7/719.pdf
#
# Find the starting position of the lexicographically smallest rotation
# of a string. Uses Booth's algorithm (O(n)).

import sys

def least_rotation(s):
    s = s + s
    n = len(s)
    f = [-1] * n
    k = 0
    for j in range(1, n):
        sj = s[j]
        i = f[j - 1 - k]
        while i != -1 and sj != s[k + i + 1]:
            if sj < s[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != s[k + i + 1]:
            if sj < s[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k

def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        pos = least_rotation(s)
        print(pos + 1)  # 1-indexed

if __name__ == "__main__":
    solve()
