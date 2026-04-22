# UVA 455 - Periodic Strings
# https://onlinejudge.org/external/4/455.pdf
#
# Find the smallest period of a string. A period p means s[i] == s[i % p]
# for all i.

import sys

def solve():
    n = int(input())
    first = True
    for _ in range(n):
        input()  # blank line
        s = input().strip()
        # Try all possible period lengths from 1 to len(s)
        length = len(s)
        for p in range(1, length + 1):
            if length % p != 0:
                continue
            valid = True
            for i in range(p, length):
                if s[i] != s[i % p]:
                    valid = False
                    break
            if valid:
                if not first:
                    print()
                first = False
                print(p)
                break

if __name__ == "__main__":
    solve()
