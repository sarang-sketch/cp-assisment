# UVA 10082 - WERTYU
# https://onlinejudge.org/external/100/10082.pdf
#
# A typist has placed hands one position to the right on a QWERTY keyboard.
# Decode by mapping each character one position to the LEFT on the keyboard row.

import sys

def solve():
    keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

    for line in sys.stdin:
        result = []
        for ch in line:
            idx = keyboard.find(ch)
            if idx > 0:
                result.append(keyboard[idx - 1])
            else:
                result.append(ch)
        print(''.join(result), end='')

if __name__ == "__main__":
    solve()
