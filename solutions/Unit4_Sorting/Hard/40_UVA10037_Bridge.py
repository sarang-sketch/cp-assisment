# UVA 10037 - Bridge
# https://onlinejudge.org/external/100/10037.pdf
#
# Classic bridge and torch problem. n people cross a bridge (max 2 at a time),
# need flashlight. Minimize total crossing time.
#
# Strategy: Sort times. Two approaches for moving the two slowest:
#   A) Fastest goes with slowest, comes back, fastest goes with 2nd slowest, comes back
#      Cost: a[n-1] + a[0] + a[n-2] + a[0]
#   B) Two fastest go first, fastest comes back, two slowest go, 2nd fastest comes back
#      Cost: a[1] + a[0] + a[n-1] + a[1]
# Pick minimum of A and B at each step.

import sys

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    cases = int(data[idx].strip()); idx += 1
    
    first_case = True
    for _ in range(cases):
        # Skip blank lines
        while idx < len(data) and data[idx].strip() == '':
            idx += 1
        
        n = int(data[idx].strip()); idx += 1
        times = []
        for i in range(n):
            times.append(int(data[idx].strip())); idx += 1
        
        times.sort()
        
        if not first_case:
            print()
        first_case = False
        
        total_time = 0
        moves = []
        remaining = list(times)
        
        while len(remaining) > 3:
            k = len(remaining)
            # Strategy A: fastest escorts each of the two slowest
            cost_a = remaining[k-1] + remaining[0] + remaining[k-2] + remaining[0]
            # Strategy B: fastest pair crosses, fastest returns, slowest pair crosses, 2nd fastest returns
            cost_b = remaining[1] + remaining[0] + remaining[k-1] + remaining[1]
            
            if cost_a <= cost_b:
                total_time += cost_a
                moves.append(f"{remaining[0]} {remaining[k-1]}")
                moves.append(f"{remaining[0]}")
                moves.append(f"{remaining[0]} {remaining[k-2]}")
                moves.append(f"{remaining[0]}")
            else:
                total_time += cost_b
                moves.append(f"{remaining[0]} {remaining[1]}")
                moves.append(f"{remaining[0]}")
                moves.append(f"{remaining[k-2]} {remaining[k-1]}")
                moves.append(f"{remaining[1]}")
            
            remaining = remaining[:-2]
        
        if len(remaining) == 3:
            total_time += remaining[0] + remaining[1] + remaining[2]
            moves.append(f"{remaining[0]} {remaining[2]}")
            moves.append(f"{remaining[0]}")
            moves.append(f"{remaining[0]} {remaining[1]}")
        elif len(remaining) == 2:
            total_time += remaining[1]
            moves.append(f"{remaining[0]} {remaining[1]}")
        elif len(remaining) == 1:
            total_time += remaining[0]
            moves.append(f"{remaining[0]}")
        
        print(total_time)
        for m in moves:
            print(m)

if __name__ == "__main__":
    solve()
