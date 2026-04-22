# UVA 612 - DNA Sorting
# https://onlinejudge.org/external/6/612.pdf
#
# Sort DNA strings by their "sortedness" (number of inversions).
# Strings with equal inversions maintain original order (stable sort).

import sys

def count_inversions(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                count += 1
    return count

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    t = int(data[idx].strip()); idx += 1
    
    first = True
    for _ in range(t):
        # Skip blank lines
        while idx < len(data) and data[idx].strip() == '':
            idx += 1
        
        n, m = map(int, data[idx].split()); idx += 1
        strings = []
        for i in range(n):
            s = data[idx].strip(); idx += 1
            inv = count_inversions(s)
            strings.append((inv, i, s))
        
        # Stable sort by inversions
        strings.sort(key=lambda x: (x[0], x[1]))
        
        if not first:
            print()
        first = False
        
        for _, _, s in strings:
            print(s)

if __name__ == "__main__":
    solve()
