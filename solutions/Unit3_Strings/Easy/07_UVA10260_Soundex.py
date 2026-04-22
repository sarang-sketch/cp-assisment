# UVA 10260 - Soundex
# https://onlinejudge.org/external/102/10260.pdf
#
# Encode each word into Soundex digits:
#   1 -> B, F, P, V
#   2 -> C, G, J, K, Q, S, X, Z
#   3 -> D, T
#   4 -> L
#   5 -> M, N
#   6 -> R
# A, E, I, O, U, H, W, Y are not represented.
# Consecutive same-code letters produce only one digit.

import sys

def soundex_code(ch):
    ch = ch.upper()
    if ch in "BFPV":
        return '1'
    if ch in "CGJKQSXZ":
        return '2'
    if ch in "DT":
        return '3'
    if ch == 'L':
        return '4'
    if ch in "MN":
        return '5'
    if ch == 'R':
        return '6'
    return '0'  # vowels and H, W, Y

def solve():
    for line in sys.stdin:
        word = line.strip()
        if not word:
            continue
        result = []
        prev = '0'
        for ch in word:
            code = soundex_code(ch)
            if code != '0' and code != prev:
                result.append(code)
            prev = code
        print(''.join(result))

if __name__ == "__main__":
    solve()
