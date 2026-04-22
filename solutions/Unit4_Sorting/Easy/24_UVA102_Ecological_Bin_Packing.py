# UVA 102 - Ecological Bin Packing
# https://onlinejudge.org/external/1/102.pdf
#
# 3 bins, each containing brown(B), green(G), clear(C) bottles.
# Assign one color to each bin. Try all 6 permutations of (B,G,C)
# to 3 bins. Minimize total moves (bottles not in assigned bin).

import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        vals = list(map(int, line.split()))
        # bin 0: B0, G0, C0 = vals[0], vals[1], vals[2]
        # bin 1: B1, G1, C1 = vals[3], vals[4], vals[5]
        # bin 2: B2, G2, C2 = vals[6], vals[7], vals[8]
        bins = [
            (vals[0], vals[1], vals[2]),
            (vals[3], vals[4], vals[5]),
            (vals[6], vals[7], vals[8])
        ]
        total = sum(vals)
        
        # Permutations: assign color to each bin
        # Colors: B=0, C=1, G=2 (alphabetical order for tiebreak)
        # Actually labels: B, C, G in alphabetical order
        perms = [
            ('B', 'C', 'G'), ('B', 'G', 'C'),
            ('C', 'B', 'G'), ('C', 'G', 'B'),
            ('G', 'B', 'C'), ('G', 'C', 'B')
        ]
        color_idx = {'B': 0, 'G': 1, 'C': 2}
        
        best_moves = float('inf')
        best_label = ""
        
        for p in perms:
            # p[i] = color assigned to bin i
            kept = 0
            for i in range(3):
                ci = color_idx[p[i]]
                kept += bins[i][ci]
            moves = total - kept
            label = ''.join(p)
            if moves < best_moves:
                best_moves = moves
                best_label = label
        
        print(best_label)

if __name__ == "__main__":
    solve()
