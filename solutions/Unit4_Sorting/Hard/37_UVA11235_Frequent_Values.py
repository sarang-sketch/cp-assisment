# UVA 11235 - Frequent Values
# https://onlinejudge.org/external/112/11235.pdf
#
# Given a sorted array, answer range queries for most frequent value.
# Encode runs, then use sparse table (RMQ) on run lengths.

import sys
import math

def solve():
    input_data = sys.stdin.buffer.read().decode()
    tokens = input_data.split()
    idx = 0
    
    while idx < len(tokens):
        n = int(tokens[idx])
        if n == 0:
            break
        q = int(tokens[idx + 1])
        idx += 2
        
        a = [int(tokens[idx + i]) for i in range(n)]
        idx += n
        
        # Build run-length encoding
        run_id = [0] * n  # which run each element belongs to
        run_start = []     # start index of each run
        run_end = []       # end index of each run
        run_len = []       # length of each run
        
        rid = 0
        run_start.append(0)
        for i in range(n):
            if i > 0 and a[i] != a[i - 1]:
                run_end.append(i - 1)
                run_len.append(run_end[-1] - run_start[-1] + 1)
                rid += 1
                run_start.append(i)
            run_id[i] = rid
        run_end.append(n - 1)
        run_len.append(run_end[-1] - run_start[-1] + 1)
        
        num_runs = len(run_len)
        
        # Build sparse table for RMQ on run_len
        if num_runs > 0:
            LOG = max(1, int(math.log2(num_runs)) + 1)
            sparse = [[0] * num_runs for _ in range(LOG + 1)]
            for i in range(num_runs):
                sparse[0][i] = run_len[i]
            for k in range(1, LOG + 1):
                for i in range(num_runs - (1 << k) + 1):
                    sparse[k][i] = max(sparse[k-1][i], sparse[k-1][i + (1 << (k-1))])
        
        def rmq(l, r):
            if l > r:
                return 0
            k = int(math.log2(r - l + 1))
            return max(sparse[k][l], sparse[k][r - (1 << k) + 1])
        
        for _ in range(q):
            i = int(tokens[idx]) - 1  # convert to 0-indexed
            j = int(tokens[idx + 1]) - 1
            idx += 2
            
            if run_id[i] == run_id[j]:
                # Same run
                print(j - i + 1)
            else:
                # Frequency of partial run at start
                freq_left = run_end[run_id[i]] - i + 1
                # Frequency of partial run at end
                freq_right = j - run_start[run_id[j]] + 1
                # Max frequency of complete runs in between
                ans = max(freq_left, freq_right)
                if run_id[i] + 1 <= run_id[j] - 1:
                    ans = max(ans, rmq(run_id[i] + 1, run_id[j] - 1))
                print(ans)

if __name__ == "__main__":
    solve()
