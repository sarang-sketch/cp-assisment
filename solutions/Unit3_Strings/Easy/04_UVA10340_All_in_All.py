# UVA 10340 - All in All
# https://onlinejudge.org/external/103/10340.pdf
#
# Check if string s is a subsequence of string t.

import sys

def is_subsequence(s, t):
    it = iter(t)
    return all(c in it for c in s)

def solve():
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue
        s, t = parts[0], parts[1]
        print("Yes" if is_subsequence(s, t) else "No")

if __name__ == "__main__":
    solve()
