# UVA 1251 - Repeated Substitution with Sed
# https://onlinejudge.org/external/12/1251.pdf
#
# BFS from target back to source (reverse direction since alpha < beta in length).
# For each state, try reverse-substituting beta with alpha.

import sys
from collections import deque

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    while idx < len(data):
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        
        pairs = []
        for _ in range(n):
            parts = data[idx].strip().split()
            idx += 1
            pairs.append((parts[0], parts[1]))
        
        gamma = data[idx].strip()  # source
        idx += 1
        delta = data[idx].strip()  # target
        idx += 1
        
        if gamma == delta:
            print(0)
            continue
        
        # BFS from gamma forward (since |alpha| < |beta|, strings grow)
        # But target might be long. Better: BFS from delta backwards
        # Replace occurrences of beta with alpha (shrinking)
        
        visited = {delta: 0}
        queue = deque([delta])
        found = False
        
        while queue:
            current = queue.popleft()
            steps = visited[current]
            
            if current == gamma:
                print(steps)
                found = True
                break
            
            if len(current) < len(gamma):
                continue
            
            # Try each substitution rule in reverse: replace beta with alpha
            for alpha, beta in pairs:
                # Find all non-overlapping occurrences of beta (leftmost)
                # and generate new string by replacing all with alpha
                pos = 0
                positions = []
                while pos <= len(current) - len(beta):
                    idx2 = current.find(beta, pos)
                    if idx2 == -1:
                        break
                    positions.append(idx2)
                    pos = idx2 + len(beta)
                
                if not positions:
                    continue
                
                # Build new string
                new_str = []
                prev = 0
                for p in positions:
                    new_str.append(current[prev:p])
                    new_str.append(alpha)
                    prev = p + len(beta)
                new_str.append(current[prev:])
                result = ''.join(new_str)
                
                if result not in visited:
                    visited[result] = steps + 1
                    if result == gamma:
                        print(steps + 1)
                        found = True
                        break
                    queue.append(result)
            
            if found:
                break
        
        if not found:
            print(-1)

if __name__ == "__main__":
    solve()
