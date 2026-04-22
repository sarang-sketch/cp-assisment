# UVA 10327 - Flip Sort
# https://onlinejudge.org/external/103/10327.pdf
#
# Count the number of inversions (bubble sort swaps needed).
# Simple O(n^2) approach since constraints are small.

import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        arr = list(map(int, input().split()))
        
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
        
        print(f"Minimum exchange operations : {count}")

if __name__ == "__main__":
    solve()
