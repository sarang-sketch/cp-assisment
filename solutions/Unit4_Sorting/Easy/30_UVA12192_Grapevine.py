# UVA 12192 - Grapevine
# https://onlinejudge.org/external/121/12192.pdf
#
# Given an N×M grid where rows and columns are non-decreasing,
# for each query (L, U), find the largest square subgrid where
# all values are in [L, U]. Binary search on each row for valid columns,
# then check feasibility of each square size.

import sys
from bisect import bisect_left, bisect_right

def solve():
    input_data = sys.stdin.buffer.read().decode()
    tokens = input_data.split()
    idx = 0
    
    while idx < len(tokens):
        n = int(tokens[idx]); m = int(tokens[idx + 1])
        idx += 2
        if n == 0 and m == 0:
            break
        
        grid = []
        for i in range(n):
            row = [int(tokens[idx + j]) for j in range(m)]
            idx += m
            grid.append(row)
        
        q = int(tokens[idx]); idx += 1
        
        for _ in range(q):
            L = int(tokens[idx]); U = int(tokens[idx + 1]); idx += 2
            
            best = 0
            for i in range(n):
                # In row i, find leftmost column with val >= L
                lo = bisect_left(grid[i], L)
                # Find rightmost column with val <= U
                hi = bisect_right(grid[i], U) - 1
                
                if lo > hi:
                    continue
                
                # Maximum possible square size starting from row i
                max_side = min(hi - lo + 1, n - i)
                
                # Binary search for largest valid square
                # A square of side s starting at (i, lo) has bottom-right at (i+s-1, lo+s-1)
                # We need grid[i+s-1][lo+s-1] <= U (since grid is non-decreasing)
                # and grid[i][lo] >= L (already guaranteed)
                left_s, right_s = 1, max_side
                ans = 0
                while left_s <= right_s:
                    mid_s = (left_s + right_s) // 2
                    # Check: square of size mid_s at (i, lo)
                    if i + mid_s - 1 < n and lo + mid_s - 1 < m and grid[i + mid_s - 1][lo + mid_s - 1] <= U:
                        ans = mid_s
                        left_s = mid_s + 1
                    else:
                        right_s = mid_s - 1
                
                best = max(best, ans)
            
            print(best)
        
        print('-')

if __name__ == "__main__":
    solve()
