# UVA 483 - Word Scramble
# https://onlinejudge.org/external/4/483.pdf
#
# Reverse the letters within each word while preserving word order.
# Words are separated by spaces.

import sys

def solve():
    for line in sys.stdin:
        line = line.rstrip('\n')
        words = line.split(' ')
        reversed_words = [w[::-1] for w in words]
        print(' '.join(reversed_words))

if __name__ == "__main__":
    solve()
