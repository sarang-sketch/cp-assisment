# UVA 1368 - DNA Consensus String
# https://onlinejudge.org/external/13/1368.pdf
#
# Given m DNA strings of length n, find the consensus string that
# minimizes total Hamming distance. For each column, pick the most
# frequent character (ties broken alphabetically: A < C < G < T).

import sys

def solve():
    t = int(input())
    for _ in range(t):
        m, n = map(int, input().split())
        strings = []
        for _ in range(m):
            strings.append(input().strip())
        
        consensus = []
        total_dist = 0
        for j in range(n):
            freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
            for i in range(m):
                freq[strings[i][j]] += 1
            # Pick character with max frequency; ties broken by alphabetical order
            best_char = max(sorted(freq.keys()), key=lambda c: freq[c])
            consensus.append(best_char)
            total_dist += m - freq[best_char]
        
        print(''.join(consensus))
        print(total_dist)

if __name__ == "__main__":
    solve()
