# UVA 621 - Secret Research
# https://onlinejudge.org/external/6/621.pdf
#
# Rules:
#   positive result: S == "1" or S == "4" or S == "78"
#   negative result: S ends with "35"
#   experiment failed: S starts with "9" and ends with "4"
#   not completed: S starts with "190"
# If ambiguous, first matching rule wins.

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
