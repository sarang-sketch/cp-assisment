# UVA 11462 - Age Sort
# https://onlinejudge.org/external/114/11462.pdf
#
# Sort ages (1-100) using counting sort for efficiency.
# Input: n ages per line, output sorted, space-separated.

import sys

def solve():
    while True:
        n = int(input())
        if n == 0:
            break
        ages = list(map(int, input().split()))
        ages.sort()
        print(' '.join(map(str, ages)))

if __name__ == "__main__":
    solve()
