# UVA 10018 - Reverse and Add
# https://onlinejudge.org/external/100/10018.pdf
#
# Repeatedly reverse a number and add it to itself until
# the result is a palindrome. Output the iteration count and the palindrome.

import sys

def solve():
    n = int(input())
    for _ in range(n):
        num = int(input())
        iterations = 0
        while True:
            rev = int(str(num)[::-1])
            num = num + rev
            iterations += 1
            s = str(num)
            if s == s[::-1]:
                break
        print(iterations, num)

if __name__ == "__main__":
    solve()
