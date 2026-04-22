# UVA 105 - The Skyline Problem
# https://onlinejudge.org/external/1/105.pdf
#
# Given building triples (L, H, R), compute the skyline silhouette.
# Use sweep line: for each x-coordinate, track the maximum height.

import sys

def solve():
    buildings = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = list(map(int, line.split()))
        buildings.append((parts[0], parts[1], parts[2]))
    
    if not buildings:
        return
    
    # Find the range of x-coordinates
    max_x = max(r for _, _, r in buildings)
    
    # Height array
    heights = [0] * (max_x + 1)
    
    for l, h, r in buildings:
        for x in range(l, r):
            heights[x] = max(heights[x], h)
    
    # Build skyline output
    result = []
    prev_h = 0
    for x in range(max_x + 1):
        if heights[x] != prev_h:
            result.append(str(x))
            result.append(str(heights[x]))
            prev_h = heights[x]
    
    print(' '.join(result))

if __name__ == "__main__":
    solve()
