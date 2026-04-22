# UVA 11512 - GATTACA
# https://onlinejudge.org/external/115/11512.pdf
#
# Find the longest repeated substring in a DNA string.
# If tie in length, choose lexicographically smallest.
# Uses suffix array approach (or simple O(n^2) with hashing for n<=1000).

import sys

def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        
        best_len = 0
        best_sub = ""
        best_count = 0
        
        # Binary search on length, or just try all lengths from large to small
        # For n<=1000, O(n^2) approach with suffix sorting works
        
        # Generate all suffixes and sort them
        suffixes = sorted(range(n), key=lambda i: s[i:])
        
        # Find longest common prefix between consecutive suffixes
        found = False
        for length in range(n - 1, 0, -1):
            if found:
                break
            # Check if any substring of this length appears >= 2 times
            subs = {}
            for i in range(n - length + 1):
                sub = s[i:i+length]
                subs[sub] = subs.get(sub, 0) + 1
            
            candidates = [(sub, cnt) for sub, cnt in subs.items() if cnt >= 2]
            if candidates:
                candidates.sort()
                best_sub = candidates[0][0]
                best_count = candidates[0][1]
                best_len = length
                found = True
        
        if best_len == 0:
            print("No repetitions found!")
        else:
            print(f"{best_sub} {best_count}")

if __name__ == "__main__":
    solve()
