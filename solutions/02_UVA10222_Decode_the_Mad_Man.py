# UVA 10222 - Decode the Mad Man
# https://onlinejudge.org/external/102/10222.pdf
#
# Replace each letter/punctuation by the character two positions
# to its left on a standard QWERTY keyboard. Convert to lowercase.

import sys

def solve():
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

    line = sys.stdin.read()
    result = []
    for ch in line:
        lower_ch = ch.lower()
        idx = keyboard.find(lower_ch)
        if idx >= 2:
            result.append(keyboard[idx - 2])
        else:
            result.append(ch)
    print(''.join(result), end='')

if __name__ == "__main__":
    solve()
