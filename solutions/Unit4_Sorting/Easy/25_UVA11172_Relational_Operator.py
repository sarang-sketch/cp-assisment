# UVA 11172 - Relational Operator
# https://onlinejudge.org/external/111/11172.pdf
#
# Given two integers, print <, =, or >.

import sys

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a < b:
            print('<')
        elif a > b:
            print('>')
        else:
            print('=')

if __name__ == "__main__":
    solve()
