# UVA 10945 - Mother Bear
# https://onlinejudge.org/external/109/10945.pdf
#
# Determine if a sentence is a palindrome, ignoring case and
# non-alphabetic characters. Stop when input line is "DONE".

import sys

def solve():
    for line in sys.stdin:
        line = line.strip()
        if line == "DONE":
            break
        cleaned = ''.join(ch.lower() for ch in line if ch.isalpha())
        if cleaned == cleaned[::-1]:
            print("You won't be eaten!")
        else:
            print("Uh oh..")

if __name__ == "__main__":
    solve()
