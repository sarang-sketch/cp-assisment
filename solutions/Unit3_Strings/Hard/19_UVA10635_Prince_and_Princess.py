# UVA 10635 - Prince and Princess
# https://onlinejudge.org/external/106/10635.pdf
#
# Find the LCS of two sequences. Since values can be up to n*n (62500),
# we convert LCS to LIS: map Prince's sequence to positions, then find
# LIS of the mapped Princess's sequence. O(n log n).

import sys
from bisect import bisect_left

def solve():
    t = int(input())
    for case in range(1, t + 1):
        n, p, q = map(int, input().split())
        prince = list(map(int, input().split()))
        princess = list(map(int, input().split()))
        
        # Map each value in Prince's sequence to its index
        pos = {}
        for i, val in enumerate(prince):
            pos[val] = i
        
        # Build sequence of Prince-indices for Princess's values
        # Only include values that appear in Prince's sequence
        seq = []
        for val in princess:
            if val in pos:
                seq.append(pos[val])
        
        # Find LIS of seq using patience sorting
        tails = []
        for x in seq:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        
        print(f"Case {case}: {len(tails)}")

if __name__ == "__main__":
    solve()
