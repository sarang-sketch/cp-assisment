# UVA 621 - Secret Research (also listed as Medium #13)
# https://onlinejudge.org/external/6/621.pdf
#
# This is the same problem as Easy #1 (UVA 621).
# Pattern classification of digit strings.
# See solution 01 for identical logic.

import sys

def solve():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if s == "1" or s == "4" or s == "78":
            print("+")
        elif s.endswith("35"):
            print("-")
        elif s.startswith("9") and s.endswith("4"):
            print("*")
        elif s.startswith("190"):
            print("?")

if __name__ == "__main__":
    solve()
