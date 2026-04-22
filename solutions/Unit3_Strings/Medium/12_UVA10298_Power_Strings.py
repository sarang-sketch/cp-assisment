# UVA 10298 - Power Strings
# https://onlinejudge.org/external/102/10298.pdf
#
# Given a string s, find the largest n such that s = a^n for some string a.
# Use KMP failure function: if len(s) % (len(s) - fail[-1]) == 0,
# the period is len(s) - fail[-1], and n = len(s) / period.

import sys

def solve():
    for line in sys.stdin:
        s = line.strip()
        if not s or s == '.':
            break
        n = len(s)
        fail = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = fail[j - 1]
            if s[i] == s[j]:
                j += 1
            fail[i] = j
        period = n - fail[-1]
        if n % period == 0:
            print(n // period)
        else:
            print(1)

if __name__ == "__main__":
    solve()
