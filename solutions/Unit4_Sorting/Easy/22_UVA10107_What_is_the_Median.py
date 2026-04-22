# UVA 10107 - What is the Median?
# https://onlinejudge.org/external/101/10107.pdf
#
# After each number is read, output the current median.
# Maintain a sorted list using bisect.insort.

import sys
from bisect import insort

def solve():
    nums = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        insort(nums, x)
        n = len(nums)
        if n % 2 == 1:
            print(nums[n // 2])
        else:
            print((nums[n // 2 - 1] + nums[n // 2]) // 2)

if __name__ == "__main__":
    solve()
