# UVA 11997 - K Smallest Sums
# https://onlinejudge.org/external/119/11997.pdf
#
# Given k sorted lists of k integers each, find the k smallest sums
# choosing exactly one element from each list.
# Merge two lists at a time using a min-heap.

import sys
import heapq

def merge_two_sorted(A, B, k):
    """Given two sorted arrays A and B of size k, return the k smallest
    pairwise sums A[i] + B[j], sorted."""
    # Min-heap: (sum, index_in_B)
    heap = []
    B.sort()
    for i in range(k):
        heapq.heappush(heap, (A[i] + B[0], 0))
    
    result = []
    for _ in range(k):
        s, j = heapq.heappop(heap)
        result.append(s)
        if j + 1 < k:
            # The next candidate from the same A[i]
            # We need to track which A[i] this came from
            # Recalculate: s - B[j] + B[j+1]
            heapq.heappush(heap, (s - B[j] + B[j + 1], j + 1))
    
    return result

def solve():
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        k = int(data[idx]); idx += 1
        lists = []
        for i in range(k):
            row = []
            for j in range(k):
                row.append(int(data[idx])); idx += 1
            row.sort()
            lists.append(row)
        
        # Merge all k lists
        result = lists[0]
        for i in range(1, k):
            result = merge_two_sorted(result, lists[i], k)
        
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()
