# UVA 10252 - Common Permutation
# https://onlinejudge.org/external/102/10252.pdf
#
# Given two strings a and b, find the longest string x (in alphabetical order)
# such that a permutation of x is a subsequence of both a and b.
# This is equivalent to taking the minimum frequency of each character.

import sys

def solve():
    lines = sys.stdin.read().splitlines()
    i = 0
    while i + 1 < len(lines):
        a = lines[i]
        b = lines[i + 1]
        i += 2

        result = []
        for c in "abcdefghijklmnopqrstuvwxyz":
            count = min(a.count(c), b.count(c))
            result.append(c * count)
        print(''.join(result))

if __name__ == "__main__":
    solve()
