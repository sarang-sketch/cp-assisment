# UVA 10810 - Ultra-QuickSort
# https://onlinejudge.org/external/108/10810.pdf
#
# Count the number of inversions using merge sort. O(n log n).

import sys

def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_count(arr[:mid])
    right, right_inv = merge_count(arr[mid:])
    
    merged = []
    inversions = left_inv + right_inv
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        arr = []
        for _ in range(n):
            arr.append(int(input()))
        _, inversions = merge_count(arr)
        print(inversions)

if __name__ == "__main__":
    solve()
