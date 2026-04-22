# UVA 591 - Box of Bricks
# https://onlinejudge.org/external/5/591.pdf
#
# Given stack heights, find minimum moves to equalize all stacks.
# Answer = sum of max(0, h[i] - avg) for all i.

import sys

def solve():
    case_num = 1
    while True:
        n = int(input())
        if n == 0:
            break
        heights = list(map(int, input().split()))
        avg = sum(heights) // n
        moves = sum(h - avg for h in heights if h > avg)
        print(f"Set #{case_num}")
        print(f"The minimum number of moves is {moves}.")
        print()
        case_num += 1

if __name__ == "__main__":
    solve()
